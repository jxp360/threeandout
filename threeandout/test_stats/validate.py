from test_stats.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
from datetime import datetime, timedelta
import time
import pytz
from django.db.models import Q

PICK_LOCKOUT_MINUTES = 10

def hasNotStarted(game, buffer=timedelta(0)):
    now = datetime.utcnow().replace(tzinfo=pytz.timezone('utc'))
    return game.kickoff.astimezone(pytz.timezone('US/Eastern')) > (now +buffer)

def validateTwoOrLessPicks(fflplayer, player,position,week):
    # Count the number of times a pick for the given FFLplayer matches the NFL player
    # Exclude the picking week because re-picking a player does not increase the number of uses
    if position == "QB":
        allUserMatches = Picks.objects.filter(fflPlayer=fflplayer,qb=player).exclude(week=week).count()
        return (allUserMatches)<=2
    if position == "RB":
        allUserMatches = Picks.objects.filter(fflPlayer=fflplayer,rb=player).exclude(week=week).count()
        return (allUserMatches)<=2
    if position == "WR":
        allUserMatches = Picks.objects.filter(fflPlayer=fflplayer,wr=player).exclude(week=week).count()
        return (allUserMatches)<=2
    if position == "TE":
        allUserMatches = Picks.objects.filter(fflPlayer=fflplayer,te=player).exclude(week=week).count()
        return (allUserMatches)<=2

def validateTwoOrLessPicksAll(fflplayer,pick,week):
    valid = (validateTwoOrLessPicks(fflplayer,pick.qb,"QB",week) and 
             validateTwoOrLessPicks(fflplayer,pick.rb,"RB",week) and 
             validateTwoOrLessPicks(fflplayer,pick.wr,"WR",week) and 
             validateTwoOrLessPicks(fflplayer,pick.te,"TE",week))
    return valid

    
def validatePlayer(week,player):
    try:
        game = NFLSchedule.objects.get(Q(week=week)&(Q(home=player.team) | Q(away=player.team)))
    except:
        return False
    return hasNotStarted(game, timedelta(minutes=PICK_LOCKOUT_MINUTES))
                         
def ValidPlayers(week,position,user):
    fflplayer = FFLPlayer.objects.get(user=user)
    players= NFLPlayer.objects.filter(position=position)
    validplayers = []
    #print "Number of Players" , len(players)
    for player in players:
        time0 = time.time()
        a = validatePlayer(week,player) 
        time1 = time.time()
        b= validateTwoOrLessPicks(fflplayer,player,position,week)
        time2 = time.time()
        #print "delta", time1-time0, time2-time1      
        if a and b:
            validplayers.append(player)
    #print "estimated total" ,(time2-time0)*len(players)
            
    return validplayers

def validatePick(week,pick):
    
    valid = (validatePlayer(week,pick.qb) and 
             validatePlayer(week,pick.rb) and 
             validatePlayer(week,pick.wr) and 
             validatePlayer(week,pick.te))
    return valid
