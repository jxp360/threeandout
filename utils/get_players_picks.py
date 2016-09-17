import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings.prod'

import threeandout.apps.ff_core.models as models

def getPlayer(name):
    player = models.NFLPlayer.objects.filter(name=name)
    print player
    return player[0]

def getWeeklyPicks(week,season_type="Regular"):

    picks = models.Picks.objects.filter(week=week,season_type=season_type)
    #for pick in picks:
    #    print "Team: %s | QB: %s | WR: %s | RB: %s | TE: %s" % (pick.fflplayer, pick.qb, pick.wr, pick.rb, pick.te) 
    return picks

def setWeeklyPicks(pick, qbid, rbid, wrid, teid):
    pass    

    
if __name__=="__main__":
    
    picks = getWeeklyPicks(3,'Postseason')
    for pick in picks:
        print "Team: %s | QB: %s | WR: %s | RB: %s | TE: %s" % (pick.fflplayer, pick.qb, pick.wr, pick.rb, pick.te) 

