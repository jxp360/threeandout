#!/bin/bash

source /home/ops/.virtualenvs/production/bin/activate

export XDG_CONFIG_HOME="/home/ops/.config"
export DJANGO_SETTINGS_MODULE="threeandout.settings.prod"

#get new data into nfldb
now=$(date +"%D::%T")
echo "$now ********************************* Running NFLDB Update at nfldb-update" >> /var/log/threeandout/nflupdate.log 2>&1

nfldb-update >> /var/log/threeandout/nflupdate.log 2>&1

#refresh our internal databases
python /data/threeandout/utils/dbhelper/syncdb.py "$@" >> /var/log/threeandout/nflupdate.log 2>&1
now=$(date +"%D::%T")
echo "$now  ******************************** Finished running NFLDB Update at nfldb-update" >> /var/log/threeandout/nflupdate.log 2>&1

