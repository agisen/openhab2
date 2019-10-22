#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import Adafruit_BMP.BMP085 as BMP085
#import Adafruit_DHT
import sys, time
from sht_sensor import Sht
from sht_sensor.sensor import ShtCRCCheckError

# constants
#DHT_PIN = 23                    # GPIO nr
#DHT_SENSOR = Adafruit_DHT.DHT22
s2 = Sht(8,11) #SCK,DATA

if __name__ == '__main__':
    if len(sys.argv) > 1:
        call = sys.argv[1].lower()

        if call == 'temp':
            temperature = None
            while temperature == None:
               try:
                   temperature = s2.read_t()
               except ShtCRCCheckError:
                   temperature = None
               if temperature == None:
                   time.sleep(1.5)
            print(temperature)

        elif call == 'hum':
            humidity = None
            while humidity == None:
               try:
                  temp = s2.read_t()
                  humidity = s2.read_rh(temp)
               except ShtCRCCheckError:
                  humidity = None
               if humidity == None:
                   time.sleep(1.5)
            print(humidity)
