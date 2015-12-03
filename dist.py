import RPi.GPIO as gpio
import time, sys, os, glob, threading, datetime

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
