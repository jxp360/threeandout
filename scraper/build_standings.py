import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import nflstats
import test_stats.models


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

def buildPlayoffStandings():
    test_stats.models.PlayoffStanding.objects.all().delete()
    
    fflplayers = test_stats.models.madePlayoffs.objects.all()

    for playoffplayer in fflplayers:
        fflplayer = playoffplayer.fflPlayer
        points=[0] *3
        for i,week in enumerate(range(18,21)):
                stat = test_stats.models.Picks.objects.filter(week=week,fflPlayer=fflplayer)
                if len(stat) == 1:
                    points[i] = stat[0].score
                elif len(stat) >1:
                    print "This shouldn't happen"
        print fflplayer.teamname,points[0],points[1],points[2]
        standing = test_stats.models.PlayoffStanding(fflPlayer=fflplayer,
                            scoretodate=points[0]+points[1]+points[2],
                            week1 = points[0],
                            week2 = points[1],
                            week3 = points[2],
                            )
        standing.save()    
