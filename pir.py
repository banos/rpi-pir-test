#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import logging
#from espeak import espeak
import subprocess

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')


logging.info ("Test ctrl+c to exit")
logging.info ("Initialising... 10sec...")

GPIO.setmode(GPIO.BCM)

PIR_PIN=4

try:
    GPIO.setup(PIR_PIN, GPIO.IN, GPIO.PUD_DOWN)

    time.sleep(10)
    logging.info ("Ready for action...")

    prev_state = False
    curr_state = False

    while True:
       prev_state = curr_state
       curr_state = GPIO.input(PIR_PIN)

       logging.debug ("%s" % curr_state)

       if curr_state != prev_state:
          new_state = "HIGH" if curr_state else "LOW"
          logging.debug ("Motion detected!!! %s" % (new_state))

          if new_state == "HIGH":
               logging.info ("Motion detected! (STATE=HIGH)")
               #espeak.synth("Step into my office")
               subprocess.call ( ["omxplayer", "-o", "hdmi", "evil_laugh.mp3"] )
          else:
               logging.info ("Reset (STATE=LOW)")

       time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    logging.info ("Goodbye.")



