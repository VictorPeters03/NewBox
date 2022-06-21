#!bin/bash
#toggle matchbox keyboard
keyboard on or off
PID=`pidof matchbox-keyboard`
if [ ! -e $PID ]; then
  killall matchbox-keyboard
  else
    matchbox-keyboard &
fi
