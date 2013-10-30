#!/bin/bash
export PYTHONPATH=/data/threeandout/threeandout:${PYTHONPATH}
if [ -f /var/log/update_week.log ]; then
    rm /var/log/update_week.log
fi
python /data/threeandout/scraper/update_week.py >& /var/log/update_week.log
