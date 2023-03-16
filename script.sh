#!/usr/bin/env bash

# set -e & pipefail to fail on any error
# set -e
# set -o pipefail

# create new dirs 
mkdir -p images music videos 

# delete log files in current dir
rm *.log

for file in *; do 
    if [ $file == *.mp3 ] || [ $file == *.flac ]
    then 
        echo "Move $file to music/"
        mv $file music/
    elif [ $file == *.jpg ] || [ $file == *.png ]
    then 
        echo "Move $file to images/"
        mv $file images/
    elif [ $file == *.avi ] || [ $file == *.mov ]
    then 
        echo "Move $file to videos/"
        mv $file videos/
    fi
done


# touch "photo.jpg, Warsaw, 2013-09-05 14:08:15"
# touch "Jay.png, London, 2015-06-20 15:13:22"
# touch "myFriends.png, Warsaw, 2013-09-05 14:07:13"
# touch "Eiffel.jpg, Paris, 2015-07-23 08:03:02"
# touch "pisatower.jpg, Paris, 2015-07-22 23:59:59"
# touch "BOB.jpg, London, 2015-08-05 00:02:03"
# touch "notredame.png, Paris, 2015-09-01 12:00:00"
# touch "me.jpg, Warsaw, 2013-09-06 15:40:22"
# touch "a.png, Warsaw, 2016-02-13 13:33:50"
# touch "b.jpg, Warsaw, 2016-01-02 15:12:22"
# touch "c.jpg, Warsaw, 2016-01-02 14:34:30"
# touch "d.jpg, Warsaw, 2016-01-02 15:15:01"
# touch "e.png, Warsaw, 2016-01-02 09:49:09"
# touch "f.png, Warsaw, 2016-01-02 10:55:32"
# touch "g.jpg, Warsaw, 2016-02-29 22:13:11"
