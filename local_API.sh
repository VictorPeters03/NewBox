#!/bin/bash
# move this file to /etc/profile.d/
cd /home/newbox/NewBox/NewBoxAPI
/usr/local/bin/uvicorn main:app --host 0.0.0.0 --reload --root-path /home/newbox/NewBox/NewBoxAPI &