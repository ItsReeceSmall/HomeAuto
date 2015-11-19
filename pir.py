import RPi.GPIO as gpio
import time, sys

# Methods
def getPir():
  print('Checking for PIR activity. . .')
  i = gpio.input(16)
  if i == 0:
    print('- Activity Undetected')
    print('- Lights OFF')
    #lights code here
  if i == 1:
    print('- Activity Detected')
    print('- Lights ON')
    #lights code here
  time.sleep(0.1)

def main():
  getPir()

gpio.setmode(gpio.BOARD)

# Pins
pirPin = 16

# Pin Setup
gpio.setup(pirPin, gpio.IN)

while True:
  main()
  time.sleep(1)

gpio.cleanup()
sys.exit()
