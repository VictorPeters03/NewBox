#!/bin/sh
# needs sudo chmod 777 API.py
/home/newbox/.local/bin/uvicorn main:app --host 0.0.0.0 &