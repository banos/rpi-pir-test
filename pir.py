#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

print "Test ctrl+c to exit"
print "Initialising..."

GPIO.setmode(GPIO.BCM)

PIR_PIN=4

GPIO.setup(PIR_PIN, GPIO.IN, GPIO.PUD_DOWN)

time.sleep(2)
print "Ready"

prev_state = False
curr_state = False

while True:
   prev_state = curr_state
   curr_state = GPIO.input(PIR_PIN)

   print "%s" % curr_state

   if curr_state != prev_state:
      new_state = "HIGH" if curr_state else "LOW"
      print "Motion detected!!! %s" % (new_state)
   time.sleep(0.1)


