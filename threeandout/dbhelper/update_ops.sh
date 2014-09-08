#!/bin/bash

source /home/ops/.virtualenvs/production/bin/activate

nfldb-update

#get new data into nfldb
now=$(date +"&D::%T")
echo "$now Running NFLDB Update at nfldb-update" >> /var/log/threeandout/nflupdate.log


#refresh our internal databases
python /data/threeandout/threeandout/dbhelper/syncdb.py "$@" &> /var/log/threeandout/nflupdate.log

