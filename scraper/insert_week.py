import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import nflstats
import test_stats.models

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

def buildStandings():
    test_stats.models.Standing.objects.all().delete()
    
    fflplayers = test_stats.models.FFLPlayer.objects.all()

    for fflplayer in fflplayers:
        points=[0] *18
        for week in range(1,18):
                stat = test_stats.models.Picks.objects.filter(week=week,fflPlayer=fflplayer)
                if len(stat) == 1:
                    points[week] = stat[0].score
                elif len(stat) >1:
                    print "This shouldn't happen"
                
        standing = test_stats.models.Standing(fflPlayer=fflplayer,
                            scoretodate=fflplayer.scoretodate,
                            week1 = points[1],
                            week2 = points[2],
                            week3 = points[3],
                            week4 = points[4],
                            week5 = points[5],
                            week6 = points[6],
                            week7 = points[7],
                            week8 = points[8],
                            week9 = points[9],
                            week10 = points[10],
                            week11 = points[11],
                            week12 = points[12],
                            week13 = points[13],
                            week14 = points[14],
                            week15 = points[15],
                            week16 = points[16],
                            week17 = points[17],
                            )
        standing.save()
    

if __name__=="__main__":
  week=3
  year = 2013
  getStats(week,year)
  buildStandings()

