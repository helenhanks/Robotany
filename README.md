# Robotany

Automated Garden Watering System. The basic system just waters the garden once per day on a schedule using water from the faucet. All the code for this is stored in `code/RobotanyMain.py`.

*Note: This project is not affiliated with the company, `Fifth Season` which was founded as `RoBotany Ltd.` It is also not related to several other projects on Github with the repository name, `Robotany`.*

## Core Features

* [Basic Raspberry Pi setup](BasicPiSetup.md)
* [Control solenoid valve](SolenoidValve.md)
* [Install Pi in waterproof enclosure](ProjectEnclosure.md)

## Optional features developed so far:

* [Add a contact level sensor to your water barrel](BarrelLevel.md)
* [Add a flow sensor to measure water usage](FlowSensor.md)
* [Query the weather API to see if it is going to rain](weatherAPI.md)
* Run a Chronjob on the Pi
* Send push notifications to your cellphone using Apprise

## Optional features not developed yet:

* Add a radar level sensor to your water barrel
* Send a push notification to a second Pi with a database to log if the job was completed
* Create a "watchdog" application to make sure the Pi Zero is always running and connected
* Build a weather station so see if it did in fact rain during the previous day
* Incorporate a water barrel with level detection and auto-filling
* [Use SmartThings API to control a smart plug connected to the solenoid valve, rather than putting a raspberry pi and relay outside](SmartThings.md)
