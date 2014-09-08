#!/bin/bash

crontab -l > tmpcron

#Set up cront job for updating stats
#Let's do it once Wednesday Morning, once Friday Morning, 3xSunday (morning, 4pm, 8pm), Monday Morning, Tuesday Morning
echo "30 04 * * 1,2,3,5,7 /data/threeandout/threeandout/dbhelpers/update_ops.sh" >> tmpcron
echo "35 04 * * 1,2,3,5,7 /data/threeandout/utils/run_update_week.sh" >> tmpcron
echo "30 12,16,20 * * 7 /data/threeandout/threeandout/dbhelpers/update_ops.sh" >> tmpcron
echo "35 12,16,20 * * 7 /data/threeandout/utils/run_update_week.sh" >> tmpcron

#Need to run auto pick one time on Sunday Morning at noon
echo "00 12 * * 7 /data/threeandout/utils/run_autopick.sh" >> tmpcron

crontab tmpcron

rm tmpcron
