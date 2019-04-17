#!/bin/bash
COUNT=1
for f in *.jpg; do
    python ClockStamp.py "$f"
    echo ${INDEX}
    let INDEX=${INDEX}+1
done

# Remove temp font
rm analogclock.ttf
echo Done!
