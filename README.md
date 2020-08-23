# Robotany

Automated Garden Watering System. The basic system just waters the garden once per day on a schedule and all the code is stored in `code/RobotanyMain.py`.

*Note: This project is not affiliated with the company, `Fifth Season` which was founded as `RoBotany Ltd.` It is also not related to several other projects on Github with the repository name, `Robotany`.*

## Core Features

* [Basic Raspberry Pi setup](BasicPiSetup.md)
* [Control solenoid valve](SolenoidValve.md)
* Install Pi in waterproof enclosure

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

## Parts

* Raspberry Pi Zero W
<img src = "images/rpi_zero.jpg" width = 200>



* Weather resistant mains power outlet with at least two outlets
<img src = "images/power_outlet.jpg" width = 200>

* Wall box for power outlet above 
<img src = "images/wall_box.jpg" width = 200>

* Mains cable and plug suitable for use outdoors
<img src = "images/extension_chord.jpg" width = 200>

* Outdoor weatherproof Enclosure
<img src = "images/enclosure.jpg" width = 200>



## Important steps

### Install Components and Wiring in Project Enclosure

_Make sure everything is powered down including 12V power supply before doing this step!_

1) Use jumper cables to hook up the Raspberry Pi pins to the Relay Module terminals
* 3.3V pin on Pi goes to VCC terminal on relay board
* Ground pin on Pi goes to GND terminal on relay board
* GPIO pin on Pi goes to VCC terminal on relay board

2) Cut the end of the 12v power supply cable and strip it
3) Cut both ends off the 12v extension cable and strip it
4) Connect 12v power supply to 12v extension cable and relay module
* Ground wire from 12V power supply gets connected to return wire of 12V cable to solenoid.
* Live wire from 12V power supply goes to COM terminal on relay board.
* Live wire from 12V cable to solenoid goes to NO terminal on relay board.

Diagram to follow. Refer to https://www.circuitbasics.com/setting-up-a-5V-relay-on-the-arduino/ for a rough idea.

5) Drill two holes in the bottom side of the box, one for the mains power cable and one for the 12V cable.
6) Cut off the outlet part of the extension cord, and strip the wire ends.
7) Install power socket into project box an connect it up with cable you just stripped through the hole you just drilled. Be sure to arrange the outlet in the box such that the 12V power supply and Raspberry Pi power supply will fit when plugged in and the box lid is closed.
6) Lay out the Raspberry Pi Zero and relay and attach to box.
7) Feed the 12V cable through the second hole so it can later be attached to the solenoid valve.
8) Finish reconnecting any remaining wires.
9) Seal up the holes in the project box using grommets if you are fancy, or silicone sealant if you are not.
10) Mount box to wall and close
11) Fit solenoind valve and water hammer arrestor directly downsteam of it.
