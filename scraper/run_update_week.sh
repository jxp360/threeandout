#!/bin/bash
now=$(date +"%D::%T")
echo "$now Running update week" >> /var/log/threeandout/update_week.log 2>&1

export PYTHONPATH="/data/threeandout/threeandout:${PYTHONPATH}"
source /home/ops/.virtualenvs/production/bin/activate

python /data/threeandout/scraper/update_week.py >> /var/log/threeandout/update_week.log 2>&1
