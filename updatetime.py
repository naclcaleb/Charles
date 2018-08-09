#!/usr/bin/python3
import time
import datetime

alarms =  ("05:45 AM")

print(alarms)
while True:
    with open('/home/pi/time.txt','r') as file:
        alarms = file.read().split(",")
    with open('/var/www/html/time.txt','w') as file:
        print(datetime.datetime.now().strftime("%I:%M %p"))
        if datetime.datetime.now().strftime("%I:%M %p") in alarms:
            file.write("true")
        else:
            file.write("false")
    time.sleep(1)
