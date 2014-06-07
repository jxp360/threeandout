import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import nflstats
import test_stats.models
from django.core.exceptions import ObjectDoesNotExist

if test_stats.models.NFLPlayer.objects.count() !=0:
  print "you already have players -- aborting insert"
  sys.exit()
else:
  print "no players in database", test_stats.models.NFLPlayer.objects.count()
s = nflstats.NflScraper()
stats = s.scrapeWeek(1,2014)
fields = ('name', 'team', 'position')
for player in stats:
  args = {}
  for scraperKey, modelKey in s.PLAYER_MAP.items():  
    args[modelKey]=player[scraperKey]
  try:
        args['team'] = test_stats.models.NFLTeam.objects.get(short_name = player['Team'])
        dbPlayer = test_stats.models.NFLPlayer(**args)
        dbPlayer.save()
  except ObjectDoesNotExist:
        if player['Team'] != 'None' : print "Team Not Found" , player['Team']




