#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Adafruit_DHT
import sys, time

sensor = Adafruit_DHT.DHT22

if __name__ == '__main__':
    if len(sys.argv) > 1:
        call = sys.argv[1].lower()

        pin = call
        temperature = None
        humidity = None

        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 1 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        while temperature == None or humidity == None or temperature > 50 or humidity > 105:
            time.sleep(1)
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        print('{:.1f}, {:.1f}'.format(temperature, humidity))

