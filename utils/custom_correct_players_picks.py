import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings.prod'

import threeandout.apps.ff_core.models as models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

def getPlayer(name):
    player = models.NFLPlayer.objects.filter(name=name)
    print player
    return player[0]

def getFFLPlayer(name):
    fflplayer = models.FFLPlayer.objects.filter(teamname=name)
    print fflplayer
    return fflplayer[0]

def getWeeklyPicks(week):

    picks = models.Picks.objects.filter(week=week)
    #for pick in picks:
    #    print "Team: %s | QB: %s | WR: %s | RB: %s | TE: %s" % (pick.fflplayer, pick.qb, pick.wr, pick.rb, pick.te) 
    return picks

def setWeeklyPick(FFLPlayer, week, season_type, qbid, rbid, wrid, teid):
    # If the user already has a pick for this week and seaon_type then don't pick
    pick = None
    try:
        pick = models.Picks.objects.get(fflplayer=FFLPlayer, week=week,season_type=season_type)[0]
        print "...Pick already exists for ", FFLPlayer.teamname
    except ObjectDoesNotExist:
        print " Making new pick"
        pick = models.Picks(week=week,season_type=season_type, fflplayer=FFLPlayer)

    pick.qb = models.NFLPlayer.objects.get(name=qbid)
    pick.rb = models.NFLPlayer.objects.get(name=rbid)
    pick.wr = models.NFLPlayer.objects.get(name=wrid)
    pick.te = models.NFLPlayer.objects.get(name=teid)

    # Validate the Pick
    pick.mod_time=timezone.now()
    pick.save()
    print "... Made pick for ", FFLPlayer.teamname
    
if __name__=="__main__":
    
    #if str(pick.fflplayer) == "Keeping Up With The Kerrigans":
    corrects = ['TheBiggestLoser', 'AutoPicks', 'Hoyer-ism', 'Autopick FTW, Inc.', 'TerrierNation', 'StaMo', 'TwoBuckChumps', 'Ravenclaws', 'Allonaprayer', 'Underwearasphyxiation', 'jack daniels']
    update = [{"Team": "Hoyer-ism", "QB": "Peyton Manning", "WR": "Demaryius Thomas", "RB": "Marshawn Lynch", "TE": "Antonio Gates"},
          {"Team": "TwoBuckChumps", "QB": "Matthew Stafford", "WR": "Antonio Brown", "RB": "Marshawn Lynch", "TE": "Martellus Bennett"},
          {"Team": "AutoPicks", "QB": "Philip Rivers", "WR": "Antonio Brown", "RB": "DeMarco Murray", "TE": "Julius Thomas"},
          {"Team": "Autopick FTW, Inc.", "QB": "Philip Rivers", "WR": "Antonio Brown", "RB": "DeMarco Murray", "TE": "Julius Thomas"},
          {"Team": "StaMo", "QB": "Philip Rivers", "WR": "Antonio Brown", "RB": "DeMarco Murray", "TE": "Julius Thomas"},
          {"Team": "Ravenclaws", "QB": "Philip Rivers", "WR": "Antonio Brown", "RB": "DeMarco Murray", "TE": "Julius Thomas"},
          {"Team": "Allonaprayer", "QB": "Philip Rivers", "WR": "Antonio Brown", "RB": "DeMarco Murray", "TE": "Julius Thomas"},
          {"Team": "Underwearasphyxiation", "QB": "Philip Rivers", "WR": "Antonio Brown", "RB": "DeMarco Murray", "TE": "Julius Thomas"},
          {"Team": "jack daniels", "QB": "Philip Rivers", "WR": "Antonio Brown", "RB": "DeMarco Murray", "TE": "Julius Thomas"},
          {"Team": "TheBiggestLoser", "QB": "Peyton Manning", "WR": "Demaryius Thomas", "RB": "Matt Forte", "TE": "Julius Thomas"}]
    for stat in update:
        fflp = getFFLPlayer(stat["Team"])
        week = 6
        season_type = "Regular"
        setWeeklyPick(fflp, week, season_type, stat['QB'], stat['RB'], stat['WR'], stat['TE'])




