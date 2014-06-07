from test_stats.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
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
def validatePlayer(week,player):
    try:
        game = NFLSchedule.objects.get(Q(week=week)&(Q(home=player.team) | Q(away=player.team)))
    except:
        return False

    return hasNotStarted(game, timedelta(minutes=PICK_LOCKOUT_MINUTES))

# Returns a list of players than could be picked by a given user on a given week.
# Used the load the table on the pick page                         
def ValidPlayers(week,position,user):
    fflplayer = FFLPlayer.objects.get(user=user)
    locktime = datetime.utcnow().replace(tzinfo=pytz.timezone('utc')) +timedelta(minutes=PICK_LOCKOUT_MINUTES)
    locktime_str = time.strftime('%Y-%m-%d %H:%M:%S',locktime.timetuple())

    # Find all NFL Players at the given position who's game has not yet started
    # Grab their score to date, home and away team for display purposes 
    # numPicked is not actually computed correctly in this query, it is just a placeholder so the object has this field later
    players= NFLPlayer.objects.raw("select test_stats_nflplayer.id, \
                                    test_stats_nflteam.name as 'teamName', \
                                    test_stats_nflplayer.name, \
                                    awayteam.name as 'away',\
                                    hometeam.name as 'home',\
                                    COUNT(test_stats_nflplayer.id) as 'numPicked', \
                                    SUM(test_stats_nflweeklystat.score) as 'scoretodate' \
                                    from test_stats_nflplayer \
                                    join test_stats_nflteam \
                                    on test_stats_nflplayer.team_id=test_stats_nflteam.id \
                                    join test_stats_nflschedule \
                                    on (test_stats_nflteam.id=test_stats_nflschedule.home_id \
                                    OR test_stats_nflteam.id=test_stats_nflschedule.away_id) \
                                    join test_stats_nflteam awayteam \
                                    on test_stats_nflschedule.away_id=awayteam.id \
                                    join test_stats_nflteam hometeam \
                                    on test_stats_nflschedule.home_id=hometeam.id \
                                    left join test_stats_nflweeklystat \
                                    on (test_stats_nflplayer.id = test_stats_nflweeklystat.player_id) \
                                    where (test_stats_nflschedule.week=%s) \
                                    AND (test_stats_nflplayer.position=%s) \
                                    AND (test_stats_nflschedule.kickoff>%s) \
                                    GROUP BY  test_stats_nflplayer.id", [week,position,locktime_str])

    # Query the Picks for this particular FFL Player
    # Exclude the current week because they are editing that week for this query 
    pickedPlayers= NFLPlayer.objects.raw("select test_stats_nflplayer.id, \
                                    COUNT(test_stats_nflplayer.id) as 'numPicked' \
                                    from test_stats_nflplayer \
                                    join test_stats_picks \
                                    on (test_stats_nflplayer.id=test_stats_picks.qb_id \
                                    OR test_stats_nflplayer.id=test_stats_picks.rb_id \
                                    OR test_stats_nflplayer.id=test_stats_picks.wr_id \
                                    OR test_stats_nflplayer.id=test_stats_picks.te_id) \
                                    where test_stats_picks.week!=%s \
                                    AND test_stats_picks.fflplayer_id=%s\
                                    GROUP BY test_stats_nflplayer.id", [week,fflplayer.id])
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

def validatePick(week,pick):
    
    valid = (validatePlayer(week,pick.qb) and 
             validatePlayer(week,pick.rb) and 
             validatePlayer(week,pick.wr) and 
             validatePlayer(week,pick.te))
    return valid
