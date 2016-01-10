#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')


logging.info ("Test ctrl+c to exit")
logging.info ("Initialising...")

GPIO.setmode(GPIO.BCM)

PIR_PIN=4

GPIO.setup(PIR_PIN, GPIO.IN, GPIO.PUD_DOWN)

time.sleep(2)
logging.info ("Ready")

prev_state = False
curr_state = False

while True:
   prev_state = curr_state
   curr_state = GPIO.input(PIR_PIN)

   logging.debug ("%s" % curr_state)

   if curr_state != prev_state:
      new_state = "HIGH" if curr_state else "LOW"
      logging.info ("Motion detected!!! %s" % (new_state))
   time.sleep(0.1)


