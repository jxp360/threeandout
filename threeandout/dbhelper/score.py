import django_env
from django.core.exceptions import ObjectDoesNotExist

models = django_env.models
import nfldb

def score(playPlayer, nflDbGame, methodName):
    """Main method to apply a scoring system in this module
    """
    meth=globals()[methodName]
    value = meth(playPlayer, nflDbGame)
    return value

def _getTeam(playPlayer,nflDbGame):
    """ helper method to get the team a player played on in a given game.
        Use this method to see what team the player WAS on the game when it was played in case they've been dropped/traded, etc.
    """
    db = nfldb.connect()
    q = nfldb.Query(db).game(gsis_id=nflDbGame.gsis_id)
    drives = q.player(player_id=player.player_id).as_drive()
    if drives:
      drive = drives[0]
      return drive.pos_team

def addIfMissing(meths):
    """Add methods to the Scoring System database
    """
    for meth in meths:
      methName = meth.__name__
      try:
        models.ScoringSystem.objects.get(function=methName)
      except ObjectDoesNotExist:
        newEntry = models.ScoringSystem(function=methName)
        newEntry.save()

def default(playPlayer, nflDbGame):
  """ default scoring system according to NFL.com
    Passing Yards: 1 point per 25 yards passing
    Passing Touchdowns: 4 points
    Interceptions: -2 points
    Rushing Yards: 1 point per 10 yards
    Rushing Touchdowns: 6 points
    Receiving Yards: 1 point per 10 yards
    Receiving Touchdowns: 6 points
    Fumble Recovered for a Touchdown: 6 points
    2-Point Conversions: 2 points
    Fumbles Lost: -2 points
  """
  twoPtConv = playPlayer.receiving_twoptm + playPlayer.rushing_twoptm
  value = 1/25.0*playPlayer.passing_yds\
        + 4*playPlayer.passing_tds\
        - 2*playPlayer.passing_int\
        + 1/10.0*playPlayer.rushing_yds\
        + 6*playPlayer.rushing_tds\
        + 1/10.0*playPlayer.receiving_yds\
        + 6*playPlayer.receiving_tds\
        + 6*playPlayer.fumbles_rec_tds\
        + 2*twoPtConv\
        - 2*playPlayer.fumbles_lost
  return value

def times2(playPlayer, nflDbGame):
  """
  """
  return 2*default(playPlayer,nflDbGame)

def _attrTimesX(playPlayer, nflDbGame,attr,X):
  score = default(playPlayer,nflDbGame)
  team = _getTeam(playPlayer,nflDbGame)
  if team== getattr(nflDbGame,attr):
    score*=X
  return score

def winnerTimes2(playPlayer, nflDbGame):
  return _attrTimesX(playPlayer, nflDbGame,'winner',2)

def looserTimes2(playPlayer, nflDbGame):
  return _attrTimesX(playPlayer,nflDbGame,'loser',2)

def homeTimes2(playPlayer,nflDbGame):
  return _attrTimesX(playPlayer, nflDbGame, 'home_team',2)

def awayTimes2(playPlayer,nflDbGame):
  return _attrTimesX(playPlayer, nflDbGame, 'away_team',2)
  
#here is where we make sure the methods are in the database
addIfMissing([default,
              times2, 
              winnerTimes2, 
              looserTimes2,
              homeTimes2,
              awayTimes2])
