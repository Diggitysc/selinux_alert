#!/bin/bash
OUTPUT="$(tail /var/log/audit/audit.log | grep denied)"
if [ -n "${OUTPUT}" ]; then
    EXECUTE="/usr/bin/python /opt/selinux_alert/hipchat_sealert.py \"SELINUX denial triggered on $(hostname)\"" 
    echo $EXECUTE
    eval $EXECUTE
fi
  
