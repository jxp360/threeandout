import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import test_stats.models
from build_standings import buildPlayoffStandings

if __name__=="__main__":
    test_stats.models.madePlayoffs.objects.all().delete()
    playoffteams = test_stats.models.Standing.objects.order_by('-scoretodate')[:10]

    for team in playoffteams:
        test_stats.models.madePlayoffs.objects.create(fflPlayer=team.fflPlayer)
    
    buildPlayoffStandings()
    