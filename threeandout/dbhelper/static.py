import django_env
models = django_env.models

import nfldb

import datetime
now = datetime.datetime.now()
CURRENT_SEASON = now.year
#IF ITS JANUARY OR FEBRUARY, ITS PART OF LAST SEASON
if now.month<3:
  CURRENT_SEASON=CURRENT_SEASON-1

TEAMS={} #keys are short abbreviation, id is django object
for team in models.NFLTeam.objects.all():
  TEAMS[team.short_name]=team

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
  q, db = getNflDbQuery()
  nfldbPlayers =[]
  for position in ('QB', 'TE', 'WR', 'RB'):
    q, db = getNflDbQuery()
    nfldbPlayers.extend(q.player(season_year=CURRENT_SEASON,position=position).as_players())
    db.close()
  djangoPlayers = models.NFLPlayer.objects.all()
  h = {}
  for player in djangoPlayers:
    h[player.nfldb_id]=player
 
  print "total players to check", len(nfldbPlayers)

  for player in nfldbPlayers:
    ID = player.profile_id
    print player.full_name 
    teamID = TEAMS[player.team]
    if ID in h:
      djangoPlayer = h[ID]
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
  print "done syncing players"

if __name__=="__main__":
  import_teams()
  sync_players()
