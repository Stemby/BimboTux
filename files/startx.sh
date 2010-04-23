#!/bin/bash
 
function check {
if [[ -f /tmp/login ]]; then
if [[ ! -f /tmp/.X0-lock ]]; then
rm /tmp/login
return 0
else
return 1
fi
else
touch /tmp/login
return 0
fi
}
 
check
 
if [[ $? -eq 0 ]]; then
 
startx 1>/dev/null 2>/dev/null
 
fi
