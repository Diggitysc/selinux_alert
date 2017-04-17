#!/bin/bash
OUTPUT="$(tail -n 1 /var/log/secure | grep opened | grep -oP '(user\s)\w+')"
if [ -n "${OUTPUT}" ]; then
     EXECUTE="/usr/bin/python /opt/selinux_alert/hipchat_useralert.py $OUTPUT 'You logged into $(hostname)'"
     eval $EXECUTE
     echo $EXECUTE >> /opt/selinux_alert/test1 
fi
