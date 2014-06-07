import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import nflschedule 
import test_stats.models
from django.core.exceptions import ObjectDoesNotExist

if test_stats.models.NFLSchedule.objects.count() !=0:
  print "you already have schedule -- aborting insert"
  sys.exit()
else:
  print "no games in database", test_stats.models.NFLPlayer.objects.count()
s = nflschedule.ScheduleScraper()
for i in xrange(1,18):
  print "doing week %s" %i
  games = s.scrapeWeek(i,2014)
  for game in games:
    args = {}
    for key in s.KEYS:  
        args['week'] = game['week']
        args['kickoff'] = game['kickoff']
        try:
            args['home'] = test_stats.models.NFLTeam.objects.get(short_name = game['home'])
        except ObjectDoesNotExist:
            print game['home']
            
        try:
            args['away'] = test_stats.models.NFLTeam.objects.get(short_name = game['away'])
        except ObjectDoesNotExist:
            print game['away']
            
    dbSchedule = test_stats.models.NFLSchedule(**args)
    dbSchedule.save()



