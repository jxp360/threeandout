import sys
sys.path.append('../threeandout')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threeandout.settings.prod')
from django.conf import settings

import nflschedule
import threeandout.apps.ff_core.models as models
from django.core.exceptions import ObjectDoesNotExist

if models.NFLTeam.objects.count() !=0:
  print "you already have teams populated -- aborting insert"
  sys.exit()
else:
  print "no teams in database", models.NFLTeam.objects.count()


TEAM_MAP = {"Vikings"   : ('MIN', 'Minnesota'),
              "Dolphins"  : ('MIA', 'Miami'),
              "Panthers"  : ('CAR', 'Carolina'),
              "Falcons"   : ('ATL', 'Atlanta'),
              "Lions"     : ('DET', 'Detroit'), 
              "Bengals"   : ('CIN', 'Cincinnati'),
              "Jets"      : ('NYJ', 'New York Jets'),
              "Broncos"   : ('DEN', 'Denver'),
              "Ravens"    : ('BAL', 'Baltimore'),
              "Giants"    : ('NYG', 'New York Giants'),
              "Raiders"   : ('OAK', 'Oakland'),
              "Titans"    : ('TEN', 'Tennessee'),
              "Saints"    : ('NO', 'New Orleans'),
              "Cowboys"   : ('DAL', 'Dallas'),
              "Patriots"  : ('NE', 'New England'),
              "Seahawks"  : ('SEA', 'Seattle'),
              "Browns"    : ('CLE', 'Cleveland'),
              "Bills"     : ('BUF', 'Buffalo'),
              "Steelers"  : ('PIT', 'Pittsburgh'),
              "Rams"      : ('STL', 'Saint Louis'),
              "Bears"     : ('CHI', 'Chicago'),
              "Texans"    : ('HOU', 'Houston'),
              "Packers"   : ('GB', 'Green Bay'),
              "Redskins"  : ('WAS', 'Washington'),
              "Jaguars"   : ('JAC', 'Jacksonville'),
              "Chiefs"    : ('KC', 'Kansas City'),
              "Eagles"    : ('PHI', 'Philadelphia'),
              "Buccaneers": ('TB', 'Tampa Bay'),
              "Colts"     : ('IND', 'Indianapolis'),
              "Cardinals" : ('ARI', 'Arizona'),
              "49ers"     : ('SF', 'San Francisco'),
              "Chargers"  : ('SD', 'San Diego') }

for key, val in TEAM_MAP.items():

    args = {}
    args['city'] = key
    args['name'] = val[1]
    args['short_name'] = val[0]
    dbTeams = models.NFLTeam(**args)
    dbTeams.save()



