import RPi.GPIO as gpio
import time, sys, os, glob, threading, datetime

def getPir(pirPin, pirLight):
  print('Checking for PIR activity. . .')
  i = gpio.input(pirPin)
  if i == 0:
    print('- Activity Undetected: Lights OFF')
    gpio.output(pirLight, gpio.HIGH) # Turns off light
  if i == 1:
    print('- Activity Detected: Lights ON')
    threading.Thread(5, gpio.output(pirLight, gpio.LOW)).start()
    #gpio.output(pirLight, gpio.LOW) # Turns on light
