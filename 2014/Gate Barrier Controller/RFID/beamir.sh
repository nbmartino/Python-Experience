#!/bin/sh
while [ 1 ]
do
echo "sending key code.."
sudo irsend -d /var/run/lirc/lircd1 SEND_ONCE myremote KEY_NUMERIC_7
done