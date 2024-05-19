import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from ClockController import *

myClock = ClockController()
  # created instance
while True:
  myClock.showTime()
  time.sleep(1)
