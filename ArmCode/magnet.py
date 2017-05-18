#!/usr/bin/python

"""https://www.raspberrypi.org/forums/viewtopic.php?f=44&t=31714"""

import wiringpi

LED  = 1 # gpio pin 12 = wiringpi no. 1 (BCM 18)

# Initialize PWM output for LED
wiringpi.wiringPiSetup()
wiringpi.pinMode(LED, 2)     # PWM mode
wiringpi.pwmWrite(LED, 0)    # OFF

# # Set LED brightness
# def led(led_value):
#     wiringpi.pwmWrite(LED,led_value)
#
# led(1)
try:
    while True:
        wiringpi.pwmWrite(LED, 1)
except:
    wiringpi.pwmWrite(LED, 0)  # OFF