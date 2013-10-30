import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import nflstats
import test_stats.models
from build_standings import buildStandings

def getStats(week, year):
  s = nflstats.NflScraper()
  stats = s.scrapeWeek(int(week),int(year))
  for player in stats:
    args = {}
    for scraperKey, modelKey in s.PLAYER_MAP.items():  
      args[modelKey]=player[scraperKey]
    dbPlayers = test_stats.models.NFLPlayer.objects.filter(**args)
    if len(dbPlayers)==1:
      statArgs={}
      for scraperKey, modelKey in s.STATS_MAP.items():
        statArgs[modelKey]=player[scraperKey]
      statArgs['player']=dbPlayers[0]
      statArgs['week']=week
      stats = test_stats.models.NFLWeeklyStat(**statArgs)
      stats.save()
    else:
      print "query %s produced %s players" %(args, len(dbPlayers))


if __name__=="__main__":
  week=5
  year = 2013
  #getStats(week,year)
  buildStandings()

