import sys, os
basedir2 = os.path.dirname(__file__)
sys.path.append(basedir2)
sys.path.append(os.path.join(basedir2, '../threeandout/dbhelper'))
sys.path.append(os.path.join(basedir2, '../threeandout'))



import django_env
models = django_env.models

def buildStandings():
    models.Standing.objects.all().delete()
    
    fflplayers = models.FFLPlayer.objects.all()
    print 'All fflplayers' 
    print fflplayers

    for fflplayer in fflplayers:
        points=[0] *18
        for week in range(1,18):
                stat = models.Picks.objects.filter(week=week,fflplayer=fflplayer,season_type="Regular")
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
        for i,week in enumerate(range(1,4)):
                stat = models.Picks.objects.filter(week=week,fflplayer=fflplayer,season_type='Postseason')
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

    #buildStandings()
    buildPlayoffStandings()

