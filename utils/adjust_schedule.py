import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings.dev' 
import threeandout.apps.ff_core.models as models
from django.core.exceptions import ObjectDoesNotExist
from threeandout.apps.ff_core.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
from datetime import datetime, timedelta
import time
import pytz


if __name__=="__main__":
    
    gameids = xrange(1,332)
    #gameids = [1]
    offset = timedelta(days=365)
    for id in gameids:
        game = NFLSchedule.objects.get(id=id)
        game.kickoff = game.kickoff + offset
        game.save()