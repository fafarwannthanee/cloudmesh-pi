from __future__ import print_function
import serial
import smbus
import math
import RPi.GPIO as GPIO
import struct
import sys
import time
from cloudmesh.pi import GPS

g = GPS()

print("warm up")
time.sleep(3)

while 1:
    [t, fix, sats, altitude, latitude, longitude] = g.get()
    print("Time : ", t)
    print("Fix satus : ", fix)
    print("Satalites in view :", sats)
    print("Altitude : ", altitude)
    print("Latitide : ", latitude)
    print("Longitude : ", longitude)
    time.sleep(2)
