import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings' 
import nflstats
import test_stats.models

if test_stats.models.NFLPlayer.objects.count() ==0:
  print "you have no players -- please run insert schedule first"
  sys.exit()
else:
  print "players in database", test_stats.models.NFLPlayer.objects.count()
s = nflstats.NflScraper()
stats = s.scrapeWeek(15,2013)
manualUpdatesNeeded=[]
for player in stats:
  args = {}
  for scraperKey, modelKey in s.PLAYER_MAP.items():  
    args[modelKey]=player[scraperKey]
  dbPlayers = test_stats.models.NFLPlayer.objects.filter(name=args['name'], position=args['position']).all()
  if any([x.team==args['team'] for x in dbPlayers]):
    #we already have him continue on
    continue
  elif len(dbPlayers)==1:
    #just one player - he must have changed teams
    #update the team and rock and roll
    thePlayer=dbPlayers[0]
    if args['team']!=thePlayer.team:
      print "updating %s from team %s" %(args, thePlayer.team)
      thePlayer.team=args['team']
      thePlayer.save()
  elif len(dbPlayers)==0:
    #we have a new player - just create a new guy and save him
    print "adding a new player", args
    dbPlayer = test_stats.models.NFLPlayer(**args)
    dbPlayer.save()
  else:
     manualUpdatesNeeded.append((args, dbPlayers))

print "updated completed"
if manualUpdatesNeeded:
  print "the following players require manual attention ..."
  for x in manualUpdatesNeeded:
    print x






