#!/usr/bin/env sh
workon production 

#get new data into nfldb
nfldb-update

#refresh our internal databases
python /data/threeandout/threeandout/dbhelper/syncdb.py "$@" 

