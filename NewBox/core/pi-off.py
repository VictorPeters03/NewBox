# Power off Pi

while True:
  if GPIO.input(GPIO_BUTTON) == 0:
    result = os.popen("sudo shutdown -h now").read()
    return
  time.sleep(0.1)

  enter