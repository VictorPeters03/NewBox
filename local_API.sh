#!/bin/bash
# move this file to /etc/profile.d/
chmod 777 /home/newbox/NewBox/NewBoxAPI/API.sh
cd /home/newbox/NewBox/NewBoxAPI
sleep 10
/usr/local/bin/uvicorn main:app --host 0.0.0.0 --reload --root-path /home/newbox/NewBox/NewBoxAPI &