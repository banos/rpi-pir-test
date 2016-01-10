#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import logging
#from espeak import espeak
import subprocess

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')


def motion_callback(PIR_PIN):
   state=GPIO.input (PIR_PIN)

   if state == 1:
       logging.info ("Motion detected ! %s" % state)
       #subprocess.call ( ["omxplayer", "-o", "hdmi", "evil_laugh.mp3"] )
       #espeak.synth("Step into my office")
   else:
       logging.info ("Reset. %s" % state)

logging.info ("Welcome to PIR test module. CTRL+C to Quit.")

PIR_PIN=4

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)

    logging.info ("Initialising... 10sec...")
    time.sleep(10)
    GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=motion_callback)
    logging.info ("Ready for action...")

    while True:
       time.sleep (100)

except KeyboardInterrupt:
    GPIO.cleanup()
    logging.info ("Goodbye.")



