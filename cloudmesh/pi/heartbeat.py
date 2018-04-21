#!/usr/bin/env python
#
# GrovePi Library for using the Grove - Finger-clip Heart Rate Sensor
# (http://www.seeedstudio.com/depot/Grove-Fingerclip-Heart-Rate-Sensor-with-shell-p-2420.html)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more
# about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this library?  Ask on the forums here:
# http://forum.dexterindustries.com/c/grovepi
#
"""
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting
Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
#############################################################################
#
# NOTE:
# The software for this sensor is still in development and might make your
# GrovePi unusable as long as this sensor is connected with the GrovePi
#
#############################################################################
import time
import sys
import RPi.GPIO as GPIO
import smbus


class HeartbeatSensor(object):
    def __init__(self):
        """
        Connect to an I2C port.
        """
        rev = GPIO.RPI_REVISION
        if rev == 2 or rev == 3:
            self.bus = smbus.SMBus(1)
        else:
            self.bus = smbus.SMBus(0)
        self.address = 0x50

    def get(self):
        """
        Returns the heart rate of the wearer.
        :return: Integer
        """
        return self.bus.read_byte(0x50)


if __name__ == "__main__":

    pulse = HeartbeatSensor()
    while True:
        try:
            rate = pulse.get()
            print(rate)
        except IOError:
            print("Error")
        time.sleep(.5)
