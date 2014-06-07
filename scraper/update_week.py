import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import nflstats
import playoffstats
import test_stats.models
from django.core.exceptions import ObjectDoesNotExist
from build_standings import buildStandings

def getStats(week, year,forcePlayoffScraper=False):
  if week >=18 or forcePlayoffScraper:
    print "using playoffstats"
    s = playoffstats.NflScraper()
  else:
    print "using regular stats"
    s = nflstats.NflScraper()
  stats = s.scrapeWeek(int(week),int(year))
  for player in stats:
    args = {}
    for scraperKey, modelKey in s.PLAYER_MAP.items():  
      try:
        args[modelKey]=player[scraperKey]
      except KeyError:
        pass
        #print 'player has no key "%s"' %scraperKey
    try:  
       args['team'] = test_stats.models.NFLTeam.objects.get(short_name = player['Team'])
       dbPlayers = test_stats.models.NFLPlayer.objects.filter(**args)
    except ObjectDoesNotExist:
       dbPlayers = []      
    if len(dbPlayers)==1:
      statArgs={}
      for scraperKey, modelKey in s.STATS_MAP.items():
        try:
          statArgs[modelKey]=player[scraperKey]
        except KeyError:
          #print 'player missing key "%s"' %scraperKey
          statArgs[modelKey]=0
      statArgs['player']=dbPlayers[0]
      statArgs['week']=week
      updateStats = test_stats.models.NFLWeeklyStat.objects.filter(player=dbPlayers[0], week=week)
      if len(updateStats) == 1:
        print 'Already found an entry for %s for week %s, so updating' % (dbPlayers[0].name, week)
        playerStat = test_stats.models.NFLWeeklyStat.objects.get(player=dbPlayers[0], week=week)
        print '%s already has %s points this week, updating to %s points' % (dbPlayers[0].name, str(playerStat.score), player['Points'])
        for scraperKey, modelKey in s.STATS_MAP.items():
          try:
            value=player[scraperKey]
          except KeyError:
            value=0
            #print 'player missing key "%s"' %scraperKey
          setattr(playerStat,modelKey, value)
     
          #tmpPS = getattr(playerStat,modelKey)
          #tmpPS = player[scraperKey]
        playerStat.save()
      elif len(updateStats) == 0:
        newstats = test_stats.models.NFLWeeklyStat(**statArgs)
        newstats.save()
      else:
        print 'Too many results... skipping this one'
    else:
      print "query %s produced %s players" %(args, len(dbPlayers))

if __name__=="__main__":
  import datetime
  startGame = datetime.datetime(2013, 9, 5, 0, 0)
  current = datetime.datetime.utcnow()
  delta = current - startGame
  week = (delta.days/7)+1
  year = 2014
  print week
  print delta 
  getStats(week,year)
  buildStandings()  
