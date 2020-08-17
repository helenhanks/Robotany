#Import libraries
import sys
import RPi.GPIO as GPIO
import datetime
import time
import apprise #Notification Service

#Get current time for start information
now = datetime.datetime.now()
print "Robotany started at:",
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Create an Apprise instance
apobj = apprise.Apprise()

#Setup Pushover notifications
apobj.add('pover://UserID@Token')

#Assign GPIO pins values and other values
pin_number1 = 4
pin_number2 = 17
RainOracle = "Rain"

#How long we want to water (15 minutes = 15*60)
water_duration = 900

#Set up pin for swithing relay and make sure it is off
GPIO.setwarnings(False) #To remove warnings
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(pin_number1, GPIO.OUT) #Set relay 1 output
GPIO.setup(pin_number2, GPIO.OUT) #Set relay 2 output
GPIO.output(pin_number1, GPIO.LOW) #Make sure relay 1 is off
GPIO.output(pin_number2, GPIO.LOW) #Make sure relay 2 is off

#Run WeatherAPI script and get "RainOracle" value (Rain/No rain)
try:
    from WeatherAPI import RainOracle
except:
    RainOracle = "No rain" #Playing safe, in case of error then watering on
    print "There was an error while checking the weather at:",
    print (now.strftime("%Y-%m-%d %H:%M:%S")),
    print RainOracle
else:
    print "Last time the weather was checked:",
    print (now.strftime("%Y-%m-%d %H:%M:%S")),
    print RainOracle
finally:
#Open valve if RainOracle = No Rain
if RainOracle == "No rain":
    GPIO.setmode(GPIO.BCM)
    GPIO.output(pin_number2, GPIO.HIGH) #Turn relay 2 on
    time.sleep(water_duration)
    GPIO.output(pin_number2, GPIO.LOW) #Turn relay 2 off
    apobj.notify(title='From Rpi-BP', body='The back Patio has been watered!',)
elif RainOracle == "Rain":
    apobj.notify(title='From Rpi-BP', body='No need to water the back Patio today!',)