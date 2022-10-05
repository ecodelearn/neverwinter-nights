#!/bin/bash

# watch tail -f -n 400 |grep -i  '"*miss*\|Gained:\|*success*\|*hit*\|"'  /mnt/c/nwn/logs/nwclientlog1.txt

# watch tail -f -n1  |grep -i  '"*miss*\|Gained:\|*success*\|*hit*\|"' /mnt/c/nwn/logs/nwclientlog1.txt

# tail /mnt/c/nwn/logs/nwclientlog1.txt |  grep -i '"*miss*\|Gained:\|*success*\|hit

# tail -f /mnt/c/nwn/logs/nwclientlog1.txt

##essse eh o correto
# tail -f n 10  /mnt/c/nwn/logs/nwclientlog1.txt |grep -i '"*miss*\|Gained:\|*success*\|*hit*\|*critical hit*\|"'

#  tail -f n 10 /mnt/c/nwn/logs/nwclientlog1.txt |grep -i '"*miss*\|Gained:\|*success*\|*hit*\|*critical hit*\|joined\|tell\|shout\|party\|dm\|\Lost item\|\Acquired Item:\|\Altar\|"'

# tail -f --200 /mnt/c/nwn/logs/nwclientLog1.txt |grep -i '"*miss*\|Gained:\|*success*\|*hit*\|*critical hit*\|joined\|tell\|shout\|party\|dm\|Lost item:\|Acquired Item:\|Altar\|"'    

# tail -f  n 10 /mnt/c/nwn/logs/nwclientlog1.txt |grep -i '"*miss*\|Gained:\|*success*\|*hit*\|*critical hit*\|joined\|tell\|shout\|party\|dm\|\Lost item\|\Acquired Item:\|\Altar\|"'

tail n 200 -f  /mnt/c/nwn/logs/nwclientlog1.txt |grep -i '"*miss*\|Gained:\|*success*\|*hit*\|*critical hit*\|joined\|tell\|shout\|party\|dm\|\Lost item\|\Acquired Item:\|\Altar:\|\You sense disappointment.\|\Experience Points Lost:\|\Killed\|"'