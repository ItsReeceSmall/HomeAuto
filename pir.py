import RPi.GPIO as gpio
import time, sys

gpio.setmode(gpio.BOARD)
pirPin = 16
gpio.setup(pirPin, gpio.IN)

def motion(pirPin):
  print('motion detected')

print('PIR test, ctrl + c to exit')
time.sleep(1)
print('Ready')

try:
  gpio.add_event_detect(pirPin,gpio.RISING,callback=MOTION)
  while:
    time.sleep(10)
except KeyboardInterrupt:
  print('Quit')
  gpio.cleanup()
  sys.exit()
