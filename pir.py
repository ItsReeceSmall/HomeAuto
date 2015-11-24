import RPi.GPIO as gpio
import time, sys, os

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

def getTemp():
  tfile = open("/sys/bus/w1/devices/10-000802824e58/w1_slave") 
  # ----------------------------
  text = tfile.read() 
  tfile.close()
  secondline = text.split("\n")[1]
  temperatureData = secondline.split(" ")[9]
  temperature = float(temperatureData[2:])
  temperature = (temperature / 1000)
  print (temperature)
  return temperature

#def getDist():

def main():
  getPir()
  getTemp()
  #getDist()
  
gpio.setmode(gpio.BOARD)

# the Pins
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
