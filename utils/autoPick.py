import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings.dev'
from threeandout.apps.ff_core.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat,Standing,PlayoffStanding
import datetime
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
    game = NFLSchedule.objects.filter(kickoff__gt=now).order_by("kickoff").first()
    week = game.week
    season_type = game.season_type
    return week,season_type

def bestPlayerAvailable(FFLPlayer,week,season_type,position):
    validplayers = ValidPlayers(week,season_type,position,FFLPlayer.user)
    for player in validplayers:
        kickoff = findGameTime(player,week,season_type)
        if datetime.date.weekday(kickoff) != 3: # Thursday Game
            return player


def autoPickWeek(FFLPlayer,week,season_type):
    
    # If the user already has a pick for this weekand seaon_type then don't pick
    try:
        Picks.objects.get(fflPlayer=FFLPlayer, week=week,season_type=season_type)
    except ObjectDoesNotExist:
        pass
    else:
        print "Pick already exists for ", FFLPlayer.teamname
        return

    pick = Picks(week=week,season_type=season_type, fflPlayer=FFLPlayer)
    pick.qb = bestPlayerAvailable(FFLPlayer,week,season_type,"QB")
    pick.rb = bestPlayerAvailable(FFLPlayer,week,season_type,"RB")
    pick.wr = bestPlayerAvailable(FFLPlayer,week,season_type,"WR")
    pick.te = bestPlayerAvailable(FFLPlayer,week,season_type,"TE")
    if validatePick(week,season_type,pick) and validateTwoOrLessPicksAll(player,pick,week):
        pick.mod_time=timezone.now()
        pick.save()    
    else:
        print "Error Invalid Auto-Pick" , FFLPlayer.teamname

if __name__=="__main__":
    
    week,season_type = findCurrentWeek()
    players = FFLPlayer.objects.all()
    for player in players:
        print player.teamname
        autoPickWeek(player,week,season_type)
    