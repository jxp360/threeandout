import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings.prod'

import threeandout.apps.ff_core.models as models

def getScoringSystem(funcName):
  return models.ScoringSystem.objects.get(function=funcName)

def getGames(week,seasonType='Regular'):
  return models.NFLSchedule.objects.filter(week=week,season_type=seasonType)


def updateScoringSystem(week,soringSystem='winnerTimes2',seasonType='Regular'):
  scoringSystem = getScoringSystem(soringSystem)
  games = getGames(week,seasonType)
  for game in games:
    game.scoring_system=scoringSystem
    game.save()

if __name__=="__main__":
  updateScoringSystem(9)
  updateScoringSystem(12)
  updateScoringSystem(15)


