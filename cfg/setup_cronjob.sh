#!/bin/bash

crontab -l > tmpcron

#Set up cront job for updating stats
#Let's do it once Wednesday Morning, once Friday Morning, 3xSunday (morning, 4pm, 8pm), Monday Morning, Tuesday Morning
echo "30 08 * * 1,2,3,5,7 /data/threeandout/utils/dbhelper/update_ops.sh" >> tmpcron
echo "36 08 * * 1,2,3,5,7 /data/threeandout/utils/scraper/run_update_week.sh" >> tmpcron
echo "30 16,20 * * 7 /data/threeandout/utils/dbhelper/update_ops.sh" >> tmpcron
echo "36 16,20 * * 7 /data/threeandout/utils/scraper/run_update_week.sh" >> tmpcron
echo "30 00 * * 1 /data/threeandout/utils/dbhelper/update_ops.sh" >> tmpcron
echo "36 00 * * 1 /data/threeandout/utils/scraper/run_update_week.sh" >> tmpcron

#Need to run auto pick one time on Sunday Morning at noon
echo "50 16 * * 7 /data/threeandout/utils/run_autoPick.sh" >> tmpcron

crontab tmpcron

rm tmpcron
