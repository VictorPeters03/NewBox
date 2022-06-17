# Power off Pi
import os
import time

import GPIO as GPIO

while True:
  if GPIO.input(GPIO_BUTTON) == 0:
    result = os.popen("sudo shutdown -h now").read()
    return
  time.sleep(0.1)

  enter