import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings'
import test_stats.models
import datetime
import pytz

def adjustTimeZones():
  eastern = pytz.timezone('US/Eastern')
  daylighSavings = datetime.datetime(2013, 11, 3, tzinfo=eastern)
  s=test_stats.models.NFLSchedule.objects.all()
  offset = datetime.timedelta(hours=1)
  print len(s)
  for game in s:
    print game.kickoff
    if game.kickoff < daylighSavings:
      print "adjusting %s vs %s week %s" %(game.home, game.away, game.week)
      game.kickoff-=offset
      game.save()

if __name__=="__main__":
  adjustTimeZones()

