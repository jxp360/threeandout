#!/bin/bash

export THREEANDOUT_DB=/data/dbs/threeandout.db

python /data/threeandout/threeandout/manage.py runserver 0.0.0.0:80
