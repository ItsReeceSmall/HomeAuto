import RPi.GPIO as gpio
import time, sys, os, glob, threading, datetime

def getPir(pirState, pirPin, pirLight):
  if pirState == 1:
    print('- Light remaining on for 10 seconds')
    time.sleep(10)
  print('Checking for PIR activity. . .')
  pirState = gpio.input(pirPin)
  if pirState == 0:
    print('- Activity Undetected: Lights OFF')
    gpio.output(pirLight, gpio.HIGH) # Turns off light
  if pirState == 1:
    print('- Activity Detected: Lights ON')
    gpio.output(pirLight, gpio.LOW) # Turns on light
  return pirState
