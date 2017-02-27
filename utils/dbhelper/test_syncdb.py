import os,sys
tmpdir = os.path.dirname(__file__)
sys.path.append(tmpdir)
sys.path.append(os.path.join(tmpdir, ".."))

import django_env
models = django_env.models

import nfldb

from django.utils import timezone
import datetime
import sys
import score

now = datetime.datetime.now()
CURRENT_SEASON = now.year
#IF ITS JANUARY OR FEBRUARY, ITS PART OF LAST SEASON
if now.month<3:
  CURRENT_SEASON=CURRENT_SEASON-1

#print "FOR DEBUG ONLY - lets use last year because it has data!"
#CURRENT_SEASON=CURRENT_SEASON-1

TEAMS={} #keys are short abbreviation, id is django object
for team in models.NFLTeam.objects.all():
  TEAMS[str(team.short_name)]=team

class Hasher(object):
  def __init__(self, dataList, attr = 'nfldb_id'):
    self.d = {}
    for data in dataList:
      key = getattr(data,attr)
      if self.d.has_key(key):
        print "hasher has duplicate key %s"%key
        print "your screwed - a human must look at this"
        sys.exit(1)
      self.d[key]=data

  def get(self, key):
    return self.d.get(key,None)

def getNflDbQuery():
  db = nfldb.connect()
  q= nfldb.Query(db)
  return q, db

def now():
  db = nfldb.connect()
  phase, season, week = nfldb.current(db)
  return {'phase':phase,
          'season':season,
          'week':week}
  db.close()

def import_teams():
  """move teams from nfldb to django model -- this should be done only once
  """
  if models.NFLTeam.objects.count()==0:
    for t in nfldb.team.teams:
      print t
      team = models.NFLTeam(short_name = t[0], city=t[1], name=t[2])
      team.save()
    print "sync done",  models.NFLTeam.objects.count()
    for team in models.NFLTeam.objects.all():
      TEAMS[team.short_name]=team

  else:
    print "teams have already been imported"

def sync_players():
  """sync players from nfldb to django model.  This can be run whenever 
  """
  print "syncing players" 
  nfldbPlayers =[]
  for position in ('QB', 'TE', 'WR', 'RB'):
    q, db = getNflDbQuery()
    nfldbPlayers.extend(q.player(position=position).as_players())
    db.close()
  hasher  = Hasher(models.NFLPlayer.objects.all())
  #djangoPlayers = models.NFLPlayer.objects.all()
  #h = {}
  #for player in djangoPlayers:
  #  h[player.nfldb_id]=player
 
  print "total players to check", len(nfldbPlayers)

  for player in nfldbPlayers:
    ID = player.player_id
    print player.full_name 
    teamID = TEAMS[player.team]
    djangoPlayer= hasher.get(ID)
    if djangoPlayer:
      #check for a team change
      #to do - update logic here if players can change position mid year - but I don't think so!
      save = djangoPlayer.team!=teamID
      if save:
        djangoPlayer.team=teamID
    else:
      #new player here
      djangoPlayer = models.NFLPlayer(name = player.full_name, team = teamID, position = str(player.position), nfldb_id=ID)
      save =True
    if save:
      djangoPlayer.save() 
  print "total players synched = %s" %models.NFLPlayer.objects.count()

def sync_schedule():
  """sync schedule from nfldb to django model.  This can be run whenever 
  """
  q, db = getNflDbQuery()
  #games=q.game(season_year=CURRENT_SEASON, season_type='Regular').as_games()
  print "for now only doing the regular season.  TBD fix that"
  games=q.game(season_year=CURRENT_SEASON).as_games()
  db.close()
  hasher = Hasher(models.NFLSchedule.objects.all())
  #djangoGames = models.NFLSchedule.objects.all()
  #d = {}
  #for game in djangoGames:
  #  d[game.nfldb_id]=game
  print "checking games", len(games)
  defaultScore = models.ScoringSystem.objects.get(function='default')
  for game in games:
    gameID = game.gsis_id
    kickoff = game.start_time
    djangoGame = hasher.get(gameID)
    if djangoGame:
      print djangoGame.season_type, djangoGame.week, djangoGame.home,  djangoGame.away, djangoGame.kickoff
      #make sure game hasn't changed times
      save = djangoGame.kickoff != kickoff
      if save:
        print "updating kickoff from %s to %s" %(djangoGame.kickoff, kickoff)
        djangoGame.kickoff = kickoff
    else:
      save = True
      homeTeam = TEAMS[str(game.home_team)]
      awayTeam = TEAMS[str(game.away_team)]
      djangoGame = models.NFLSchedule(home =homeTeam, away =awayTeam, week = game.week, season_type=game.season_type, kickoff = kickoff, nfldb_id = gameID, scoring_system=defaultScore)
    if save:
      djangoGame.save()
  print "total games in schedule = %s"%models.NFLSchedule.objects.count()

class StatSyncher(object):
  #key is django key
  #value is nfldb key
  MAP = {'recTd'             : 'receiving_tds',
         'fumbles'           : 'fumbles_lost',
         'interceptions'     : 'passing_int',
         'passTd'            : 'passing_tds',
         'passYds'           : 'passing_yds',
         'fumbleRecoveryTDs' : 'fumbles_rec_tds',
         'rushYds'           : 'rushing_yds',
         'recYds'            : 'receiving_yds',
         'rushTd'            : 'rushing_tds'}
  def __init__(self):
    self.playerHasher = Hasher(models.NFLPlayer.objects.all())

  def sync_game(self, djangoGame,forceRescore=False):
    db = nfldb.connect()
    q = nfldb.Query(db)
    gameID = djangoGame.nfldb_id
    print "**** gameID %s *****" %gameID
    print "game = %s - %s week %s " %(djangoGame, djangoGame.season_type, djangoGame.week)
    q.game(gsis_id=gameID)
    nflDbGame = q.as_games()[0]
    hasStarted = nflDbGame.is_playing or nflDbGame.finished
    if not hasStarted:
      return 
    players = q.as_players()
    for player in players:
      if player.position.name in ("QB", "WR", "TE", "RB"):
        q = nfldb.Query(db).game(gsis_id=gameID)
        gameStats = q.player(player_id=player.player_id).as_aggregate()
        assert(len(gameStats)==1)
        playPlayer=gameStats[0] 

        print "ID = ", playPlayer.player_id, playPlayer.player.full_name, playPlayer.player.team 
        djangoPlayer      = self.playerHasher.get(playPlayer.player_id)
        if djangoPlayer==None:
          print "SOMETHING HAS GONE VERY WRONG HERE.  A human must look at this!"
          continue
        
        res = models.NFLWeeklyStat.objects.filter(player = djangoPlayer, game=djangoGame)
        count = res.count()
        if count==0:       
          print('#player has no score for that game already')
          pts = score.score(playPlayer, nflDbGame, djangoGame.scoring_system.function)
          if djangoGame.scoring_system.function !="default":
             defaultScore = score.default(playPlayer, nflDbGame)
          else:
             defaultScore = pts
          d={'score'        : pts,
             'player'       : djangoPlayer,
             'game'         : djangoGame,
             'defaultScore' : defaultScore}
          for key, value in self.MAP.items():
            d[key] =getattr(playPlayer,value)
          
          djangoStat = models.NFLWeeklyStat(**d)
          print ('Saving Stat ',djangoStat,djangoStat.score,djangoStat.game)
          djangoStat.save()
        elif count==1:
          print ('#update stats if required')
          save = False
          djangoStat = res.get()
          print '###########################################'
          print djangoStat, djangoStat.player.id, djangoStat.id, djangoStat.score
          print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'


          for key, value in self.MAP.items():
            newVal = getattr(playPlayer,value)
            oldVal = getattr(djangoStat, key)
            if newVal!=oldVal:
              setattr(djangoStat,key,newVal)
              save = True
          if save or forceRescore:          
            pts = score.score(playPlayer, nflDbGame, djangoGame.scoring_system.function)
            if pts!= djangoStat.score:
              djangoStat.score=pts
              save=True
            if djangoGame.scoring_system.function !="default":
              defaultScore = score.default(playPlayer, nflDbGame)
            else:
              defaultScore = pts
            if defaultScore != djangoStat.defaultScore:
              djangoStat.defaultScore=defaultScore
              save=True
          print pts, djangoStat.score, defaultScore, djangoStat.defaultScore
          if save:
            print "saving the data"
            djangoStat.save()
    db.close()
  def sync_games(self, forceRescore=False, **filterargs):
    if filterargs:
      games = models.NFLSchedule.objects.filter(**filterargs)
    else:
      games = models.NFLSchedule.objects.all()
    for game in games:
      self.sync_game(game,forceRescore)

  def syncAll(self,maxWeek=19):
    for i in xrange(1,maxWeek+1):
      self.sync_week(i)

  def getMatchingWeek(self, gamedate):
    early_date = gamedate - datetime.timedelta(days=2)
    late_date = gamedate + datetime.timedelta(days=4)
    games = models.NFLSchedule.objects.filter(kickoff__gte=early_date, kickoff__lte=late_date)
    print len(games)
    week = 44
    for game in games:
      if game.week < week:
        week = game.week
    print "Found week = %d" % week
    return week
  

if __name__=="__main__":
  #import_teams()
  #sync_schedule()
  
  #sync_players()
  ss = StatSyncher()
  #curr = timezone.now()
  #week = ss.getMatchingWeek(curr)
  #ss.sync_games(forceRescore=True, week=week, season_type="Regular")
  ss.sync_games(forceRescore=True, week=1, season_type="Postseason")
