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
  program(pirPin, pirLight, trigL, echoL, trigR, echoR)

def program(pirPin, pirLight, trigL, echoL, trigR, echoR):
  print('calling pir to get light detection')
  threading.Thread(pir.getPir(pirPin, pirLight)).start()
  outDist = dist.getDist(trigL, echoL)
  print (outDist)
  time.sleep(1)
  inDist = dist.getDist(trigR, echoR)
  print (inDist)
  
main()

gpio.cleanup()
sys.exit()
