# Import Libraries
import RPi.GPIO as GPIO
import datetime
import time

# Define variables and assign values
relay_pin_number = 3
low_level_pin_number = 8
high_level_pin_number = 12

# Initialise water counter
counter = 0
max_water_minutes = 30

#Set up pin for switching relay and make sure it is off
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin_number, GPIO.OUT)
GPIO.output(relay_pin_number, False)

#Set up pins for measuring low level
GPIO.setup(low_level_pin_number, GPIO.IN)
GPIO.setup(high_level_pin_number, GPIO.IN)

while True:
    
    # Repeat loop every minute
    time.sleep(60)
    
    # Check low level, switch off tap if it sees water
    if GPIO.input(low_level_pin_number) > 0.5:
        GPIO.output(relay_pin_number, False)
        counter = 0
        print("Barrel level is above low detector, turning off water")
    
    # Turn off water if it has been filling for 30 minutes
    elif counter >= max_water_minutes:
        GPIO.output(relay_pin_number, False)
        print("Barrel level is still low after 30 minutes, turning off water")
    
    # Check low level, switch on tap if it does not see water
    elif GPIO.input(low_level_pin_number) < 0.5:
        GPIO.output(relay_pin_number, True)
        counter = counter + 1
        print("Barrel level is low, turning on water")
        

