import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
  
from test_stats.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
import time
from datetime import datetime, timedelta
import time
import pytz
from django.db.models import Q
from test_stats.validate import *
PICK_LOCKOUT_MINUTES = 10
from django.contrib.auth.models import User


if __name__=="__main__":

    user = User.objects.get(username="gbf")

    for i in xrange(1,4):
        time1 = time.time()
        myValidPlayers = ValidPlayers(i,"QB",user)
        time2 = time.time()
        print "Valid QBs " , len(myValidPlayers)
        print "ValidPlayers on QBs " , time2-time1