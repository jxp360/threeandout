import django_env
from django.core.exceptions import ObjectDoesNotExist

models = django_env.models


def score(playPlayer, nflDbGame, methodName):
    meth=globals()[methodName]
    value = meth(playPlayer, nflDbGame)
    return value

def addIfMissing(meths):
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

addIfMissing([default,times2])
