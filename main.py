import RPi.GPIO as gpio
import time, sys, os, glob, threading, datetime
import pir
import dist
#import temp
'''
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = golb.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1-slave'
'''
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
    threading.Timer(2, dist.getDist(trigL, echoL)).start()
    time.sleep(3.333)
    threading.Timer(2, dist.getDist(trigR, echoR)).start()
  
main()

gpio.cleanup()
sys.exit()
