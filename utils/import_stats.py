import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings'

import test_stats.models


def importCsv(csvFileName):

  fields = test_stats.models.NFLWeeklyStat._meta.get_all_field_names()
  fields.extend(['player.name','player.team','player.position'])

  f = file(csvFileName,'r')
  lines = [x.strip() for x in f.readlines()]
  f.close()
  hdr = lines[0].split(',')
  columns = {}
  for i, key in enumerate(hdr):
    columns[key]=i
  columns.pop('id')
  s1 = set(fields)
  s2 = set(columns.keys())
  s2.add('id')
  if s1 !=s2:
    if s1-s2 !='player' and not (s2-s1):
      print "not all keys are present"
      print s1-s2
      print s2-s1
      return 
  for line in lines[1:]:
    l=line.split(',')
    tmp={}  
    for key, index in columns.items():
      tmp[key]=l[index]
    try:
        playerID = tmp.pop('player')
    except KeyError:
        playerID = None
    playerName = tmp.pop('player.name')
    playerTeam=tmp.pop('player.team')
    playerPosition = tmp.pop('player.position')

    if playerID:
      player = test_stats.models.NFLPlayer.objects.get(id=playerID)
      assert(player.name==playerName)
      assert(player.team==playerTeam)
      assert(player.position==playerPosition)
    else:           
      result = test_stats.models.NFLPlayer.objects.get(name=playerName, team=playerName, position=playerPosition)
      assert(len(result)==1)
      player = result[0]
    tmp['player']=player
    updateStats = test_stats.models.NFLWeeklyStat.objects.filter(player=player, week=tmp['week'])
    if len(updateStats) == 1:
      print 'Already found an entry for %s for week %s, so updating' % (player.name, tmp['week'])
      playerStat = updateStats[0]
      for key, value in tmp.items():
        if key !='player':
          try:
            value=tmp[key]
          except KeyError:
            value=0
            #print 'player missing key "%s"' %scraperKey
          setattr(playerStat,key, value)

      playerStat.save()
    elif len(updateStats) == 0:
      newstats = test_stats.models.NFLWeeklyStat(**tmp)
      newstats.save()
    else:
      print 'Too many results... skipping this one'   

if __name__=="__main__":
  importCsv('tmp.csv')
