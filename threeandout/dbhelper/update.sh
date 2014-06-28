#!/usr/bin/env sh

#get new data into nfldb
/usr/local/bin/nfldb-update

#refresh our internal databases
python syncdb.py "$@" 

