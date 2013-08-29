import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import nflschedule 
import test_stats.models

if test_stats.models.NFLSchedule.objects.count() !=0:
  print "you already have schedule -- aborting insert"
  sys.exit()
else:
  print "no games in database", test_stats.models.NFLPlayer.objects.count()
s = nflschedule.ScheduleScraper()
for i in xrange(1,18):
  print "doing week %s" %i
  games = s.scrapeWeek(i,2013)
  for game in games:
    args = {}
    for key in s.KEYS:  
      args[key]=game[key]
    dbSchedule = test_stats.models.NFLSchedule(**args)
    dbSchedule.save()



