#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import Adafruit_BMP.BMP085 as BMP085
#import Adafruit_DHT
import sys, time
from sht_sensor import Sht

# constants
#DHT_PIN = 23                    # GPIO nr
#DHT_SENSOR = Adafruit_DHT.DHT22
sensor = Sht(14,4)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        call = sys.argv[1].lower()

        if call == 'temperature':
            temperature = None
            while temperature == None:
               #_, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
               temperature = sensor.read_t()
               if temperature == None:
                   time.sleep(1.5)
            print(temperature)

        elif call == 'humidity':
            humidity = None
            while humidity == None:
               #humidity, _ = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
               temp = sensor.read_t()
               humidity = sensor.read_rh(temp)
               if humidity == None:
                   time.sleep(1.5)
            print(humidity)

#        elif call == 'pressure':
#            sensor = BMP085.BMP085()
#            print(sensor.read_pressure() / 100.0)
