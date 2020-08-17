# Import Libraries
import datetime
import time
import apprise

# Create an Apprise instance
apobj = apprise.Apprise()

# Setup Pushover notification
apobj.add('pover://UserID@Token')

#Notification every x hours based on crontab
apobj.notify(title='From Rpi-BP', body='RPi-BP is online!',)
now = datetime.datetime.now()
print 'Rpi-BP is online as of:',
print (now.strftime("%Y-%m-%d %H:%M:%S"))