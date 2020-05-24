# Import Libraries
import RPi.GPIO as GPIO
import datetime
import time

# Define variables and assign values
pin_number = 8
start_hour = 6
start_minute = 0
water_duration = 5*60 # = 5 minutes

#Set up pin for swithing relay and make sure it is off
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.OUT)
GPIO.output(pin_number, False)

# Calculate water end time
end_hour = (start_hour + int(water_duration/3600))%24
end_minute = (start_minute + int(water_duration/60))%60

while True:
    
    # Repeat loop every minute
    time.sleep(60)
    
    # Get current time
    now = datetime.datetime.now()
    
    # Set today's watering start and end time
    start_time = now.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    end_time = now.replace(hour=end_hour, minute=end_minute, second=0, microsecond=0)
    
    # Check current time against start and end times
    if now < start_time:
        GPIO.output(pin_number, False)
    elif now > start_time and now < end_time:
        GPIO.output(pin_number, True)
    elif now > end_time:
        GPIO.output(pin_number, False)