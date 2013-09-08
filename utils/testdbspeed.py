import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
  
from test_stats.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
from test_stats.validate import *
import time

if __name__=="__main__":
    
    #QBs = NFLPlayer.objects.filter(position="QB")

    for i in xrange(10):
        time1 = time.time()
        allPlayers = NFLPlayer.objects.all()
        for player in allPlayers:
            validatePlayer(1,player)
        time2 = time.time()
        print "ValidatePlayer on all Players takes " , time2-time1