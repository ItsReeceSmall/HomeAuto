import RPi.GPIO as gpio
import time, sys, os, glob, threading
import datetime
'''
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = golb.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1-slave'
'''
# Methods
def printit():
  threading.Timer(5.0, getPir).start()
  print ("Hello World!")
  print ('-------------')
  time.sleep(1)

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

def getDist(TRIG, ECHO):
    #This is a pre written method which checks an ultrasonic sensor that is connected to the pi
    #So the pins will be imported depending which sensor is running in the while loop further down
    gpio.setup(TRIG,gpio.OUT)
    gpio.setup(ECHO,gpio.IN)
    gpio.output(TRIG, False)
    #print "Waiting For Sensor To Settle"
    time.sleep(0.2)
    gpio.output(TRIG, True)
    time.sleep(0.00001)
    gpio.output(TRIG, False)
    while gpio.input(ECHO)==0:
      pulse_start = time.time()
    while gpio.input(ECHO)==1:
      pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    #print ("Distance: " + str(distance) + "cm")
    return distance

def main():
  printit()
  #getPir()
  #getTemp()
  #outDist = getDist(trigL, echoL)
  #print (outDist)
  #inDist = getDist(trigR, echoR)
  #print (inDist)
  
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

while True:
  main()

gpio.cleanup()
sys.exit()
