import RPi.GPIO as gpio
import time, sys

gpio.setmode(gpio.BOARD)
pirPin = 16
gpio.setup(pirPin, gpio.IN)

def motion(pirPin):
  print('motion detected')
  time.sleep(1)

while True:
    i = gpio.input(16)
    if i == 0:
        print('No Intruders' + str(i))
        time.sleep(0.1)
    if i == 1:
        print('Intruder Detected' + str(i))
        time.sleep(0.1)

gpio.cleanup()
sys.exit()
