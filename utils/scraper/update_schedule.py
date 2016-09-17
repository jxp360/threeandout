import sys
sys.path.append('../threeandout')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threeandout.settings.dev')
from django.conf import settings

import nflschedule 
import threeandout.apps.ff_core.models as ff_core_models
import pytz
import datetime
from django.core.exceptions import ObjectDoesNotExist 

if ff_core_models.NFLSchedule.objects.count() ==0:
  print "you already have schedule -- aborting update.  Please run insert first"
  sys.exit()
else:
  print "games in database", ff_core_models.NFLPlayer.objects.count()
s = nflschedule.ScheduleScraper()

eastern = pytz.timezone('US/Eastern')
daylighSavings = datetime.datetime(2015, 11, 3, tzinfo=eastern)
offset = datetime.timedelta(hours=1)

for i in xrange(1,18):
  print "doing week %s" %i
  games = s.scrapeWeek(i,2015)
  for game in games:
    args = {}
    for key in s.KEYS:  
      args[key]=game[key]
    try:
      theGame = ff_core_models.NFLSchedule.objects.get(week=args['week'], home=args['home'], away =args['away'])
    except ObjectDoesNotExist:
      print "cannot find game",  args
    else:
      if args['kickoff'] < daylighSavings:
        args['kickoff']-=offset
      newGame = ff_core_models.NFLSchedule(**args)
      if newGame.kickoff!=theGame.kickoff:
        print "adjusing %s to %s, %s vs %s" %(theGame.kickoff, newGame.kickoff, theGame.home, theGame.away) 
        theGame.kickoff=newGame.kickoff
        theGame.save()



