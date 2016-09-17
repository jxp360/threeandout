#!/usr/bin/env python

''' This file can delete a specific team's weekly picks and deletes it.  '''

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

def getWeeklyPicks(week):

    picks = models.Picks.objects.filter(week=week)
    #for pick in picks:
    #    print "Team: %s | QB: %s | WR: %s | RB: %s | TE: %s" % (pick.fflplayer, pick.qb, pick.wr, pick.rb, pick.te) 
    return picks

    
if __name__=="__main__":
    
    picks = getWeeklyPicks(9)
    for pick in picks:
        
        
        #if str(pick.fflplayer) == "Keeping Up With The Kerrigans":
        #corrects = ['TheBiggestLoser', 'AutoPicks', 'Hoyer-ism', 'Autopick FTW, Inc.', 'TerrierNation', 'StaMo', 'TwoBuckChumps', 'Ravenclaws', 'Allonaprayer', 'Underwearasphyxiation', 'jack daniels']
        #if str(pick.fflplayer) in corrects:
        #if pick.qb == models.NFLPlayer.objects.get(name="Andrew Luck") \
        #   and pick.wr == models.NFLPlayer.objects.get(name="Antonio Brown") \
        #   and pick.rb == models.NFLPlayer.objects.get(name="Arian Foster") \
        #   and pick.te == models.NFLPlayer.objects.get(name=""):
            print "Team: %s | QB: %s | WR: %s | RB: %s | TE: %s" % (pick.fflplayer, pick.qb, pick.wr, pick.rb, pick.te)
            pick.delete()






