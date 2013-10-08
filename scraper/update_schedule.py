import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import nflschedule 
import test_stats.models
import pytz
import datetime
from django.core.exceptions import ObjectDoesNotExist 

if test_stats.models.NFLSchedule.objects.count() ==0:
  print "you already have schedule -- aborting update.  Please run insert first"
  sys.exit()
else:
  print "games in database", test_stats.models.NFLPlayer.objects.count()
s = nflschedule.ScheduleScraper()

eastern = pytz.timezone('US/Eastern')
daylighSavings = datetime.datetime(2013, 11, 3, tzinfo=eastern)
offset = datetime.timedelta(hours=1)

for i in xrange(5,18):
  print "doing week %s" %i
  games = s.scrapeWeek(i,2013)
  for game in games:
    args = {}
    for key in s.KEYS:  
      args[key]=game[key]
    try:
      theGame = test_stats.models.NFLSchedule.objects.get(week=args['week'], home=args['home'], away =args['away'])
    except ObjectDoesNotExist:
      print "cannot find game",  args
    else:
      if args['kickoff'] < daylighSavings:
        args['kickoff']-=offset
      newGame =test_stats.models.NFLSchedule(**args)
      if newGame.kickoff!=theGame.kickoff:
        print "adjusing %s to %s, %s vs %s" %(theGame.kickoff, newGame.kickoff, theGame.home, theGame.away) 
        theGame.kickoff=newGame.kickoff
        theGame.save()



