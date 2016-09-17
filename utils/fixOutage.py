import sys, os

basedir = os.path.dirname(__file__)
sys.path.append(basedir)
sys.path.append(os.path.join(basedir, '../threeandout/dbhelper'))
sys.path.append(os.path.join(basedir, '../threeandout'))
import django_env

from threeandout.apps.ff_core.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
import datetime,time
import pytz
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from threeandout.apps.ff_core.validate import ValidPlayers, validatePick,validateTwoOrLessPicksAll
import csv

def findGameTime(player,week,season_type):
    try:
        game = NFLSchedule.objects.get(Q(home=player.team) | Q(away=player.team),week=week,season_type=season_type)
    except:
        # Player has not game
        return None
    return game.kickoff

def findDefinedWeek():
    now = datetime.datetime(2015,11,1,0,0,0,0,pytz.timezone('utc'))
    game = NFLSchedule.objects.filter(kickoff__gt=now).order_by("kickoff").first()
    week = game.week
    season_type = game.season_type
    return week,season_type

def findCurrentWeek():
    now = datetime.datetime(2015,11,1,0,0,0,0,pytz.timezone('utc'))
    #now = datetime.datetime.utcnow().replace(tzinfo=pytz.timezone('utc'))
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
    bestPlayersNames['QB'] = "Aaron Rodgers"
    bestPlayersNames['RB'] = "DeMarco Murray"
    bestPlayersNames['WR'] = "Demaryius Thomas"
    bestPlayersNames['TE'] = "Jimmy Graham"

    bestPlayers = {}
    for position in bestPlayersNames.keys():
        #print bestPlayersNames[position]
        bestPlayers[position] = NFLPlayer.objects.get(name=bestPlayersNames[position])
    
    return bestPlayers

def manualOverridePick(playersNames):
    players = {}
    for position in playersNames.keys():
        #print bestPlayersNames[position]
        try:
            players[position] = NFLPlayer.objects.get(name=playersNames[position])
        except ObjectDoesNotExist, e:
            print "Could not find player name for %s" % playersNames[position]
            raise e
    return players


def manPickWeek(FFLPlayer, week, season_type, picks):
    # If the user already has a pick for this week and seaon_type then don't pick
    try:
        Picks.objects.get(fflplayer=FFLPlayer, week=week,season_type=season_type)
    except ObjectDoesNotExist:
        pass
    else:
        print "...Pick already exists for ", FFLPlayer.teamname
        return

    pick = Picks(week=week,season_type=season_type, fflplayer=FFLPlayer,autopick=False)
    
    # For the first week of the season just the best players from last year
    bestPlayerAvailable = manualOverridePick(picks)       
    pick.qb = bestPlayerAvailable["QB"]
    pick.rb = bestPlayerAvailable["RB"]
    pick.wr = bestPlayerAvailable["WR"]
    pick.te = bestPlayerAvailable["TE"]
   
    # Validate the Pick
    if validateTwoOrLessPicksAll(player,pick,week):
        pick.mod_time=timezone.now()
        pick.save()    
        print "... Made pick for ", FFLPlayer.teamname
        print "QB: %s  RB: %s  WR: %s  TE: %s" % (pick.qb, pick.rb, pick.wr, pick.te)
    else:
        print "Error Invalid Man-Pick, no Pick made" , FFLPlayer.teamname

def autoPickWeek(FFLPlayer,week,season_type):
    
    # If the user already has a pick for this week and seaon_type then don't pick
    try:
        Picks.objects.get(fflplayer=FFLPlayer, week=week,season_type=season_type)
    except ObjectDoesNotExist:
        pass
    else:
        print "...Pick already exists for ", FFLPlayer.teamname
        return

    pick = Picks(week=week,season_type=season_type, fflplayer=FFLPlayer,autopick=False)
    
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
    
    week,season_type = findDefinedWeek()
    print "Manually making picks for week %s for season type %s" % (week, season_type)
    players = FFLPlayer.objects.all()
    if len(sys.argv) != 3:
        print "Expecting \"python fixOutage.py CSV_PICKS_FILE.txt --smettings=prod\""
        sys.exit()

    filename = sys.argv[-1]
    if not os.path.exists(filename):
        print "Could not find file %s" % filename
        sys.exit()

    print "Reading data from file %s" % filename
    csvpicks = {}
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            try:
                csvpicks[row[0]] = {"QB": row[1], "RB": row[2], "WR": row[3], "TE":row[4]}
            except IndexError, e:
                print "Reached end of file"
     
    #Check if user exists
    for key, val in csvpicks.items():
        try:
            player = FFLPlayer.objects.get(teamname=key)
            print "FFLPlayer found for team %s" % key
            manPickWeek(player, week, season_type, val)    
        except ObjectDoesNotExist:
            print "No FFLPlayer found for team %s; trying display name" % key
            try:
                player = FFLPlayer.objects.get(displayName=key)
            except ObjectDoesNotExist:
                print "No FFLPlayer found for name %s" % key
           

    #for player in players:
    #        print "Making Pick for" % time.asctime() , player.teamname,
    #        autoPickWeek(player,week,season_type)

    
