import sys
sys.path.append('../threeandout')
import os
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings'

import test_stats.models


def getCsv(week,csvFileName):

  statsSorter = [(x.player.name,x.player.team,x) for x in test_stats.models.NFLWeeklyStat.objects.filter(week=week)]
  statsSorter.sort()
  stats = [x[-1] for x in statsSorter]
  
  fields = test_stats.models.NFLWeeklyStat._meta.get_all_field_names()
  fields.sort()
  fields.remove('id')
  fields.insert(0,'id')
  fields.remove('player')
  fields.insert(1,'player')
  print "dumping %s stats" %len(stats)  
  hdr=fields[:]
  #adding extra fields to the header
  hdr.insert(2,'player.name')
  hdr.insert(3,'player.team')
  hdr.insert(4,'player.position') 
  hdrStr=','.join([str(x) for x in hdr])+"\n"
  f = file(csvFileName,'w')
  f.write(hdrStr)
  for stat in stats:
    tmp=[]
    for key in fields:
      if key=='player':
        tmp.append(str(stat.player.id))
        tmp.append(str(stat.player.name))
        tmp.append(str(stat.player.team))
        tmp.append(str(stat.player.position))
      else:
        tmp.append(str(getattr(stat,key)))         
    s=','.join(tmp)+"\n"
    f.write(s)

  f.close()

if __name__=="__main__":
  getCsv(18,'tmp.csv')
