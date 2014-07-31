import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings.dev' 
import nflstats
import threeandout.apps.ff_core.models as models


def buildStandings():
    models.Standing.objects.all().delete()
    
    fflplayers = models.FFLPlayer.objects.all()
    print 'All fflplayers' 
    print fflplayers

    for fflplayer in fflplayers:
        points=[0] *21
        for week in range(1,21):
                stat = models.Picks.objects.filter(week=week,fflplayer=fflplayer)
                if len(stat) == 1:
                    points[week] = stat[0].score
                elif len(stat) >1:
                    print "This shouldn't happen"
                
        standing = models.Standing(fflplayer=fflplayer,
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

def buildPlayoffStandings():
    models.PlayoffStanding.objects.all().delete()
    
    fflplayers = models.madePlayoffs.objects.all()

    for playoffplayer in fflplayers:
        fflplayer = playoffplayer.fflplayer
        points=[0] *3
        for i,week in enumerate(range(18,21)):
                stat = models.Picks.objects.filter(week=week,fflplayer=fflplayer)
                if len(stat) == 1:
                    points[i] = stat[0].score
                elif len(stat) >1:
                    print "This shouldn't happen"
        print fflplayer.teamname,points[0],points[1],points[2]
        standing = models.PlayoffStanding(fflplayer=fflplayer,
                            scoretodate=points[0]+points[1]+points[2],
                            week1 = points[0],
                            week2 = points[1],
                            week3 = points[2],
                            )
        standing.save()    

if __name__ == "__main__":

    buildStandings()
