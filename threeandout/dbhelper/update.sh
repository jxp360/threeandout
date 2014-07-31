#!/usr/bin/env sh

#get new data into nfldb
nfldb-update

#refresh our internal databases
python syncdb.py "$@" 

