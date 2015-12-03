import RPi.GPIO as gpio
import time, sys, os, glob, thrreading, datetime

def getPir(pirPin, pirLight):
  print('Checking for PIR activity. . .')
  i = gpio.input(pirPin)
  if i == 0:
    print('- Activity Undetected: Lights OFF')
    gpio.output(pirLight, gpio.LOW) # Turns off light
  if i == 1:
    print('- Activity Detected: Lights ON')
    gpio.output(pirLight, gpio.HIGH) # Turns on light
  time.sleep(0.05)
  return i
