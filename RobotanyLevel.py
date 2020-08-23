# Import Libraries
import RPi.GPIO as GPIO

# Define variables and assign values
level_pin_number = 8


#Set up pin for swithing relay and make sure it is off
GPIO.setmode(GPIO.BOARD)
GPIO.setup(level_pin_number, GPIO.IN)

# Test Sensor
print(GPIO.input(level_pin_number))



