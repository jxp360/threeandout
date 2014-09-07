#!/bin/bash

source /home/ops/.virtualenvs/production/bin/activate

export PYTHONPATH=/data/threeandout/threeandout:${PYTHONPATH}
python /data/threeandout/utils/autoPick.py --settings=prod >& /var/log/threeandout/autoPick.log
