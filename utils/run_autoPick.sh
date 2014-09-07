#!/bin/bash

source /home/ops/.virtualenvs/production/bin/activate

export PYTHONPATH=/data/threeandout/threeandout:${PYTHONPATH}
if [ -f /var/log/autoPick.log ]; then
    rm /var/log/autoPick.log
fi
python /data/threeandout/utils/autoPick.py >& /var/log/autoPick.log
