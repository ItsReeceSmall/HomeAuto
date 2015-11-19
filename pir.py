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
    gpio.output(pirLight, gpio.HIGH)
  if i == 1:
    print('- Activity Detected')
    print('- Lights ON')
    #lights code here
    gpio.output(pirLight, gpio.LOW)
  time.sleep(0.1)

#def getTemp():

def main():
  getPir()

gpio.setmode(gpio.BOARD)

# Pins
pirPin = 16
pirLight = 18

# Pin Setup
gpio.setup(pirPin, gpio.IN)
gpio.setup(pirLight, gpio.OUT)

while True:
  main()
  time.sleep(1)

gpio.cleanup()
sys.exit()
