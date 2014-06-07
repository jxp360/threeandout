import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings.dev' 
import nflschedule 
import threeandout.apps.ff_core.models as models
from django.core.exceptions import ObjectDoesNotExist

if models.NFLSchedule.objects.count() !=0:
  print "you already have schedule -- aborting insert"
  sys.exit()
else:
  print "no games in database", models.NFLPlayer.objects.count()
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
            args['home'] = models.NFLTeam.objects.get(short_name = game['home'])
        except ObjectDoesNotExist:
            print game['home']
            
        try:
            args['away'] = models.NFLTeam.objects.get(short_name = game['away'])
        except ObjectDoesNotExist:
            print game['away']
            
    dbSchedule = models.NFLSchedule(**args)
    dbSchedule.save()



