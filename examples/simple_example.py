#!/usr/bin/env python3
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

GPIO.setwarnings(False)   # Disabled GPIO Set Warning
GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
hx = HX711(dout_pin=5, pd_sck_pin=6)  # create an object
print(hx.get_raw_data_mean())  # get raw data reading from hx711
GPIO.cleanup()
