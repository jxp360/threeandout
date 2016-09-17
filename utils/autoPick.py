import sys, os

basedir = os.path.dirname(__file__)
sys.path.append(basedir)
sys.path.append(os.path.join(basedir, 'dbhelper'))
sys.path.append(os.path.join(basedir, '../threeandout'))
import django_env

from threeandout.apps.ff_core.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
import datetime,time
import pytz
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from threeandout.apps.ff_core.validate import ValidPlayers, validatePick,validateTwoOrLessPicksAll


def findGameTime(player,week,season_type):
    try:
        game = NFLSchedule.objects.get(Q(home=player.team) | Q(away=player.team),week=week,season_type=season_type)
    except:
        # Player has not game
        return None
    return game.kickoff

def findCurrentWeek():
    now = datetime.datetime.utcnow().replace(tzinfo=pytz.timezone('utc'))
    #game = NFLSchedule.objects.filter(~Q(season_type="Regular"),kickoff__gt=now).order_by("kickoff").first()
    game = NFLSchedule.objects.filter(kickoff__gt=now).order_by("kickoff").first()
    week = game.week
    season_type = game.season_type
    return week,season_type

def bestPlayerAvailable(FFLPlayer,week,season_type,position):
    validplayers = ValidPlayers(week,season_type,position,FFLPlayer.user)
    validplayers.sort(key=lambda x: x.scoretodate, reverse=True)
    for player in validplayers:
        kickoff = findGameTime(player,week,season_type)
        if datetime.date.weekday(kickoff) != 3: # Thursday Game
            return player

def manualPick():
    bestPlayersNames ={}
    # 2013 Points Leaders at their positions
    bestPlayersNames['QB'] = "Russell Wilson"
    bestPlayersNames['RB'] = "Devonta Freeman"
    bestPlayersNames['WR'] = "Antonio Brown"
    bestPlayersNames['TE'] = "Rob Gronkowski"

    bestPlayers = {}
    for position in bestPlayersNames.keys():
        #print bestPlayersNames[position]
        bestPlayers[position] = NFLPlayer.objects.get(name=bestPlayersNames[position])
    
    return bestPlayers


def autoPickWeek(FFLPlayer,week,season_type):
    
    # If the user already has a pick for this week and seaon_type then don't pick
    try:
        Picks.objects.get(fflplayer=FFLPlayer, week=week,season_type=season_type)
    except ObjectDoesNotExist:
        pass
    else:
        print "...Pick already exists for ", FFLPlayer.teamname
        return

    # Don't auto pick if plyer already has 3 autopicks 
    numautopick = Picks.objects.filter(fflplayer=FFLPlayer,season_type=season_type,autopick=True).count()
    if numautopick >= 3 :
        print "... Player already has three auto picks"
        return

    pick = Picks(week=week,season_type=season_type, fflplayer=FFLPlayer,autopick=True)
    
    # For the first week of the season just the best players from last year
    if week==1 and season_type=="Regular":
        bestPlayers = manualPick()
        pick.qb = bestPlayers["QB"]
        pick.rb = bestPlayers["RB"]
        pick.wr = bestPlayers["WR"]
        pick.te = bestPlayers["TE"]  
    
    else:
        pick.qb = bestPlayerAvailable(FFLPlayer,week,season_type,"QB")
        pick.rb = bestPlayerAvailable(FFLPlayer,week,season_type,"RB")
        pick.wr = bestPlayerAvailable(FFLPlayer,week,season_type,"WR")
        pick.te = bestPlayerAvailable(FFLPlayer,week,season_type,"TE")
   
    # Validate the Pick
    if validatePick(week,season_type,pick) and validateTwoOrLessPicksAll(player,pick,week):
        pick.mod_time=timezone.now()
        pick.save()    
        print "... Made pick for ", FFLPlayer.teamname
        print "QB: %s  RB: %s  WR: %s  TE: %s" % (pick.qb, pick.rb, pick.wr, pick.te)
    else:
        print "Error Invalid Auto-Pick, no Auto Pick made" , FFLPlayer.teamname


if __name__=="__main__":
    
    week,season_type = findCurrentWeek()
    players = FFLPlayer.objects.all()
    for player in players:
        if player.autoPickPreference:
            print "%s Making Auto Pick for" % time.asctime() , player.teamname,
            autoPickWeek(player,week,season_type)
        else:
	    print "%s Team does not want AutoPick" % time.asctime() , player.teamname

    
