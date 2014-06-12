import django_env
models = django_env.models

import nfldb

import datetime
import sys

now = datetime.datetime.now()
CURRENT_SEASON = now.year
#IF ITS JANUARY OR FEBRUARY, ITS PART OF LAST SEASON
if now.month<3:
  CURRENT_SEASON=CURRENT_SEASON-1

print "FOR DEBUG ONLY - lets use last year because it has data!"
CURRENT_SEASON=CURRENT_SEASON-1

TEAMS={} #keys are short abbreviation, id is django object
for team in models.NFLTeam.objects.all():
  TEAMS[team.short_name]=team

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
  else:
    print "teams have already been imported"

def sync_players():
  """sync players from nfldb to django model.  This can be run whenever 
  """
  print "syncing players" 
  nfldbPlayers =[]
  for position in ('QB', 'TE', 'WR', 'RB'):
    q, db = getNflDbQuery()
    nfldbPlayers.extend(q.player(season_year=CURRENT_SEASON,position=position).as_players())
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
      djangoPlayer = models.NFLPlayer(name = player.full_name, team = teamID, position = player.position.value, nfldb_id=ID)
      save =True
    if save:
      djangoPlayer.save() 
  print "total players synched = %s" %models.NFLPlayer.objects.count()

def sync_schedule():
  """sync schedule from nfldb to django model.  This can be run whenever 
  """
  q, db = getNflDbQuery()
  #games=q.game(season_year=CURRENT_SEASON, season_type='Regular').as_games()
  games=q.game(season_year=CURRENT_SEASON).as_games()
  db.close()
  hasher = Hasher(models.NFLSchedule.objects.all())
  #djangoGames = models.NFLSchedule.objects.all()
  #d = {}
  #for game in djangoGames:
  #  d[game.nfldb_id]=game
  print "checking games", len(games)
  for game in games:
    gameID = game.gsis_id
    kickoff = game.start_time
    djangoGame = hasher.get(gameID)
    if djangoGame:
      #make sure game hasn't changed times
      save = djangoGame.kickoff != kickoff
      if save:
        print "updating kickoff from %s to %s" %(djangoGame.kickoff, kickoff)
        djangoGame.kickoff = kickoff
    else:
      save = True
      homeTeam = TEAMS[game.home_team]
      awayTeam = TEAMS[game.away_team]
      djangoGame = models.NFLSchedule(home =homeTeam, away =awayTeam, week = game.week, kickoff = kickoff, nfldb_id = gameID)
    if save:
      djangoGame.save()
  print "total games in schedule = %s"%models.NFLSchedule.objects.count()

class StatSyncher(object):
  def __init__(self):
    self.playerHasher = Hasher(models.NFLPlayer.objects.all())

  def sync_game(self, djangoGame, scoreGame):
    db = nfldb.connect()
    q = nfldb.Query(db)
    gameID = djangoGame.nfldb_id
    print "**** gameID %s *****" %gameID
    q.game(gsis_id=gameID)
    gameStats=q.as_aggregate()
    nflDbGame = q.as_games()[0]
    for playPlayer in gameStats:
      print "ID = ", playPlayer.player_id, playPlayer.player.full_name 
      if playPlayer.player.position.name in ("QB", "WR", "TE", "RB"):
        djangoPlayer      = self.playerHasher.get(playPlayer.player_id)
        if djangoPlayer==None:
          print "SOMETHING HAS GONE VERY WRONG HERE.  A human must look at this!"
          continue
        
        res = models.NFLWeeklyStat.objects.filter(player = djangoPlayer, game=djangoGame)
        count = res.count()
        if count==0:       
          #new player
          score = scoreGame(playPlayer, nflDbGame)
          djangoStat = models.NFLWeeklyStat(score             = score,
                                     recTd             = playPlayer.receiving_tds,
                                     fumbles           = playPlayer.fumbles_tot,
                                     interceptions     = playPlayer.passing_int,
                                     passTd            = playPlayer.passing_tds,
                                     passYds           = playPlayer.passing_yds,
                                     fumbleRecoveryTDs = playPlayer.fumbles_rec_tds,
                                     rushYds           = playPlayer.rushing_yds,
                                     recYds            = playPlayer.receiving_yds,
                                     rushTd            = playPlayer.rushing_tds,
                                     player            = djangoPlayer,
                                     game              = djangoGame)
          djangoStat.save()
        elif count==1:
          #update stats if required
          save = False
          djangoStat = res.get()
          if djangoStat.recTd             != playPlayer.receiving_tds:
             djangoStat.recTd              = playPlayer.receiving_tds
             save = True
          if djangoStat.fumbles           != playPlayer.fumbles_tot:
             djangoStat.fumbles            = playPlayer.fumbles_tot
             save = True
          if djangoStat.interceptions     != playPlayer.passing_int:
             djangoStat.interceptions      = playPlayer.passint_int
             save = True
          if djangoStat.passTd            != playPlayer.passing_tds:
             djangoStat.passTd             = playPlayer.passing_tds
             save = True
          if djangoStat.passYds           != playPlayer.passing_yds:
             djangoStat.passYds            = playPlayer.passing_yds
             save = True
          if djangoStat.fumbleRecoveryTDs != playPlayer.fumbles_rec_tds:
             djangoStat.fumbleRecoveryTDs  = playPlayer.fumbles_rec_tds
             save = True
          if djangoStat.rushYds           != playPlayer.rushing_yds:
             djangoStat.rushYds            = playPlayer.rushing_yds
             save = True
          if djangoStat.recYds            != playPlayer.receiving_yds:
             djangoStat.recYds             = playPlayer.receiving_yds
             save = True
          if djangoStat.rushTd            != playPlayer.rushing_tds:
             djangoStat.rushTd             = playPlayer.rushing_tds
             save = True
          if save:
            djangoStat.score = scoreGame(playPlayer, nflDbGame)
            djangoStat.save()
    db.close()
  def sync_week(self, weekNum):
    games = models.NFLSchedule.objects.filter(week=weekNum)
    scoreGame = self.getScoreSystem(weekNum)
    for game in games:
      self.sync_game(game, scoreGame)


  def syncAll(self,maxWeek=19):
    for i in xrange(1,maxWeek+1):
      self.sync_week(i)

  def getScoreSystem(self, weekId):
    def noPoints(*args):
      return 0
    return noPoints

if __name__=="__main__":
  import_teams()
  sync_players()
  sync_schedule()
  game = models.NFLSchedule.objects.all()[0]
  def null(*args):
    return 9
  ss = StatSyncher()
  #ss.sync_game(game,null)
  ss.sync_week(2)


