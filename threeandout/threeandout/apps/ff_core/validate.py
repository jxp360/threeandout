from threeandout.apps.ff_core.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
from datetime import datetime, timedelta
import time
import pytz
from django.db.models import Q
from django.db.models import Count,Sum

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

# Validate a give player's game has not started when picked
# Used to validate when a pick is submitted    
def validatePlayer(week,season_type,player):
    try:
        game = NFLSchedule.objects.get(Q(week=week)&Q(season_type=season_type)&(Q(home=player.team) | Q(away=player.team)))
    except:
        return False

    return hasNotStarted(game, timedelta(minutes=PICK_LOCKOUT_MINUTES))

# Returns a list of players than could be picked by a given user on a given week.
# Used the load the table on the pick page                         
def ValidPlayers(week,season_type,position,user):
    fflplayer = FFLPlayer.objects.get(user=user)
    locktime = datetime.utcnow().replace(tzinfo=pytz.timezone('utc')) +timedelta(minutes=PICK_LOCKOUT_MINUTES)
    locktime_str = time.strftime('%Y-%m-%d %H:%M:%S',locktime.timetuple())

    # Find all NFL Players at the given position who's game has not yet started
    # Grab their score to date, home and away team for display purposes 
    # numPicked is not actually computed correctly in this query, it is just a placeholder so the object has this field later
    players= NFLPlayer.objects.raw("select ff_core_nflplayer.id, \
                                    ff_core_nflteam.name as 'teamName', \
                                    ff_core_nflplayer.name, \
                                    awayteam.name as 'away',\
                                    hometeam.name as 'home',\
                                    COUNT(ff_core_nflplayer.id) as 'numPicked', \
                                    SUM(ff_core_nflweeklystat.score) as 'scoretodate' \
                                    from ff_core_nflplayer \
                                    join ff_core_nflteam \
                                    on ff_core_nflplayer.team_id=ff_core_nflteam.id \
                                    join ff_core_nflschedule \
                                    on (ff_core_nflteam.id=ff_core_nflschedule.home_id \
                                    OR ff_core_nflteam.id=ff_core_nflschedule.away_id) \
                                    join ff_core_nflteam awayteam \
                                    on ff_core_nflschedule.away_id=awayteam.id \
                                    join ff_core_nflteam hometeam \
                                    on ff_core_nflschedule.home_id=hometeam.id \
                                    left join ff_core_nflweeklystat \
                                    on (ff_core_nflplayer.id = ff_core_nflweeklystat.player_id) \
                                    where (ff_core_nflschedule.week=%s) \
                                    AND (ff_core_nflschedule.season_type=%s) \
                                    AND (ff_core_nflplayer.position=%s) \
                                    AND (ff_core_nflschedule.kickoff>%s) \
                                    GROUP BY  ff_core_nflplayer.id", [week,season_type,position,locktime_str])

 
    # Query the Picks for this particular FFL Player
    # Exclude the current week because they are editing that week for this query 
    pickedPlayers= NFLPlayer.objects.raw("select ff_core_nflplayer.id, \
                                    COUNT(ff_core_nflplayer.id) as 'numPicked' \
                                    from ff_core_nflplayer \
                                    join ff_core_picks \
                                    on (ff_core_nflplayer.id=ff_core_picks.qb_id \
                                    OR ff_core_nflplayer.id=ff_core_picks.rb_id \
                                    OR ff_core_nflplayer.id=ff_core_picks.wr_id \
                                    OR ff_core_nflplayer.id=ff_core_picks.te_id) \
                                    where  not (ff_core_picks.week=%s AND ff_core_picks.season_type=%s) \
                                    AND ff_core_picks.season_type!=%s \
                                    AND ff_core_picks.fflplayer_id=%s \
                                    GROUP BY ff_core_nflplayer.id", [week,season_type,"Preseason",fflplayer.id])
    
    
    validplayers = []
    pickedPlayerDict = {}
    count = 0 
    for player in pickedPlayers:
        pickedPlayerDict[player.id] =player
    # Remove the players picked more than three times from the list of all players and load numPicked 
    for player in players:
        count+=1
        if player.id in pickedPlayerDict:
                player.numPicked = pickedPlayerDict[player.id].numPicked
                if player.numPicked <3:
                    validplayers.append(player)
        #Player has never been picked by this FFLPlayer
        else:
            player.numPicked = 0    
            validplayers.append(player)             
    return validplayers

def validatePick(week,season_type,pick):
    
    valid = (validatePlayer(week,season_type,pick.qb) and 
             validatePlayer(week,season_type,pick.rb) and 
             validatePlayer(week,season_type,pick.wr) and 
             validatePlayer(week,season_type,pick.te))
    return valid
