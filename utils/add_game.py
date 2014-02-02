import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings'
import test_stats.models
import datetime
import pytz


eastern = pytz.timezone('US/Eastern')
daylighSavings = datetime.datetime(2013, 11, 3, tzinfo=eastern)
offset = datetime.timedelta(hours=1)
VALID_TEAMS=['MIN','MIA','CAR','ATL','DET','CIN','NYJ','DEN','BAL','NYG','OAK','TEN','NO','DAL','NE','SEA','CLE','BUF','PIT','STL','CHI','HOU','GB','WAS','JAC','KC','PHI','TB','IND','ARI','SF','SD']

def insertGame(homeTeam,awayTeam,week,year=2014,month=1,day=1,hour=12,minute=0): 
  """insert a game into the schedule.  
     homeTeam and awayTeam are the 2 or 3 letter strings for the nfl team playing
     week is the integer week of the season (starts with 18 for playoffs)
     year, month, day,hour,and minute are the values associated with kickoff as integers (hour is 24 hours) in the eastern time zone
     
  """
  if not homeTeam in VALID_TEAMS: 
    print "aborting insertion --homeTeam %s is invalid"
    return
  if not awayTeam in VALID_TEAMS:
    print "aborting insertion --awayTeam %s is invalid"
    return
  kickoff = datetime.datetime(year, month, day, hour, minute, tzinfo=eastern)
  #adjust for daylight savings if required
  if kickoff < daylighSavings:
      kickoff-=offset
  
  dbSchedule = test_stats.models.NFLSchedule(week=week,
                                             home=homeTeam,
                                             away=awayTeam,
                                             kickoff=kickoff)
  dbSchedule.save()

def insertGames(week,games):
  print "trying to insert %s games" %len(games)
  dbGames = test_stats.models.NFLSchedule.objects.filter(week=week)
  if len(dbGames)!=0:
    print "you already have %s games inserted for week %s - aborting insertion"%(len(dbGames), week)
    return
  for game in games:
    insertGame(week=week,**game)  
  dbGames = test_stats.models.NFLSchedule.objects.filter(week=week)
  print "you have inserted %s games" %len(games)  

if __name__=="__main__":
  #This is set-up for the 2013 season (2014 playoffs)
  #change PLAYOFF_WEEK and update the games list for each week to do the insertion
  PLAYOFF_WEEK=3

  year=2014
  month=1
  Chiefs='KC'
  Colts='IND'
  Saints='NO'
  Eagles='PHI'
  Chargers='SD'
  Bengals='CIN'
  Fourtyniners='SF'
  Packers='GB'
  Patriots='NE'
  Broncos='DEN'
  Seahawks='SEA'
  Panthers='CAR'
  TBD='TBD'
  if PLAYOFF_WEEK==1:
    games=[{'homeTeam':Colts,'awayTeam':Chiefs,'year':year,'month':month,'day':4,'hour':16,'minute':35},
           {'homeTeam':Eagles,'awayTeam':Saints,'year':year,'month':month,'day':4,'hour':20,'minute':10},
           {'homeTeam':Bengals,'awayTeam':Chargers,'year':year,'month':month,'day':5,'hour':13,'minute':5},
           {'homeTeam':Packers,'awayTeam':Fourtyniners,'year':year,'month':month,'day':5,'hour':16,'minute':40}]

  elif PLAYOFF_WEEK==2:
    #fill this out when 2nd week of playoff schedule is available
    games=[{'homeTeam':Patriots,'awayTeam':Colts,'year':year,'month':month,'day':11,'hour':20,'minute':15},
           {'homeTeam':Broncos,'awayTeam':Chargers,'year':year,'month':month,'day':12,'hour':16,'minute':40},
           {'homeTeam':Seahawks,'awayTeam':Saints,'year':year,'month':month,'day':11,'hour':16,'minute':35},
           {'homeTeam':Panthers,'awayTeam':Fourtyniners,'year':year,'month':month,'day':12,'hour':13,'minute':05}]

  elif PLAYOFF_WEEK==3:
    #fill this out when 3rd week of playoff schedule is available
    games=[{'homeTeam':Broncos,'awayTeam':Patriots,'year':year,'month':month,'day':19,'hour':15,'minute':00},
           {'homeTeam':Seahawks,'awayTeam':Fourtyniners,'year':year,'month':month,'day':19,'hour':18,'minute':30}]

  else:
    print "invalid PLAYOF_WEEK %s" %PLAYOFF_WEEK
    games=[]
  week=17+PLAYOFF_WEEK 
  insertGames(week,games)

