#!/bin/bash
# move this file to /etc/profile.d/
chmod 777 /home/newbox/NewBox/NewBoxAPI/API.sh
sleep 5
cd /home/newbox/NewBox/NewBoxAPI
/usr/local/bin/uvicorn main:app --host 0.0.0.0 --reload --root-path /home/newbox/NewBox/NewBoxAPI &