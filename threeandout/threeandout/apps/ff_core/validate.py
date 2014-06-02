from apps.ff_core.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
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
    locktime = datetime.utcnow().replace(tzinfo=pytz.timezone('utc')) +timedelta(minutes=PICK_LOCKOUT_MINUTES)
    locktime_str = time.strftime('%Y-%m-%d %H:%M:%S',locktime.timetuple())
    
    players= NFLPlayer.objects.raw("select ff_core_nflplayer.id,ff_core_nflplayer.name, \
                                    ff_core_nflplayer.team,ff_core_nflschedule.home,ff_core_nflschedule.away,\
                                    COUNT(ff_core_nflplayer.id) as 'numPicked', \
                                    SUM(ff_core_nflweeklystat.score) as 'scoretodate' \
                                    from ff_core_nflplayer \
                                    join ff_core_nflschedule \
                                    on (ff_core_nflplayer.team=ff_core_nflschedule.home \
                                    OR ff_core_nflplayer.team=ff_core_nflschedule.away) \
                                    join ff_core_nflweeklystat \
                                    on (ff_core_nflplayer.id = ff_core_nflweeklystat.player_id) \
                                    where (ff_core_nflschedule.week=%s) \
                                    AND (ff_core_nflplayer.position=%s) \
                                    AND (ff_core_nflschedule.kickoff>%s) \
                                    GROUP BY  ff_core_nflplayer.id", [week,position,locktime_str])
         
            
    pickedPlayers= NFLPlayer.objects.raw("select ff_core_nflplayer.id, \
                                    COUNT(ff_core_nflplayer.id) as 'numPicked' \
                                    from ff_core_nflplayer \
                                    join ff_core_picks \
                                    on (ff_core_nflplayer.id=ff_core_picks.qb_id \
                                    OR ff_core_nflplayer.id=ff_core_picks.rb_id \
                                    OR ff_core_nflplayer.id=ff_core_picks.wr_id \
                                    OR ff_core_nflplayer.id=ff_core_picks.te_id) \
                                    where ff_core_picks.week!=%s \
                                    AND ff_core_picks.fflplayer_id=%s\
                                    GROUP BY ff_core_nflplayer.id", [week,fflplayer.id])
    validplayers = []
    # For each possible player check how often they have been picked 
    for player in players:
        for pickedPlayer in pickedPlayers:
            if player.id == pickedPlayer.id:
                player.numPicked = pickedPlayer.numPicked
                if player.numPicked <3:
                    validplayers.append(player)
                break
        #Player has never been picked
        else:
            player.numPicked = 0    
            validplayers.append(player)   
                
                  
    return validplayers

def validatePick(week,pick):
    
    valid = (validatePlayer(week,pick.qb) and 
             validatePlayer(week,pick.rb) and 
             validatePlayer(week,pick.wr) and 
             validatePlayer(week,pick.te))
    return valid
