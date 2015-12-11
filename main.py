import RPi.GPIO as gpio
import time, sys, os, glob, threading, datetime
import pir
import dist
import temp

# Methods
def main():
  # Board setup    
  gpio.setmode(gpio.BOARD)
  # the Pins
  pirPin = 16
  pirLight = 18
  trigL = 38
  echoL = 36
  trigR = 37
  echoR = 35
  # Pin Setup
  gpio.setup(pirPin, gpio.IN)
  gpio.setup(pirLight, gpio.OUT)
  # variable setup
  program(pirPin, pirLight, trigL, echoL, trigR, echoR)

def program(pirPin, pirLight, trigL, echoL, trigR, echoR):
  pirState = 0
  while True:
    state = pir.getPir(pirState, pirPin, pirLight)
    pirState = state
    threading.Thread(target=dist.getDist, args=(trigL, echoL,)).start()
    time.sleep(2)
    threading.Thread(target=dist.getDist, args=(trigR, echoR,)).start()
    time.sleep(2)
    print(temp.read_temp())
  
main()

gpio.cleanup()
sys.exit()
