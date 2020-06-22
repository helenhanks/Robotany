# Robotany
Automated Garden Watering System. The basic system just waters the garden once per day on a schedule and all the code is stored in RobotanyMain.py

I am working on some optional extras but they are not integrated into the main script yet:

* Query the weather API to see if it is going to rain
* Send a push notification to a second Pi with a database to log if the job was completed
* Create a "watchdog" application to make sure the Pi Zero is always running and connected
* Build a weather station so see if it did in fact rain during the previous day
* Incorporate a water barrel with level detection and auto-filling
* Use SmartThings API to control a smart plug connected to the solenoid valve, rather than putting a raspberry pi and relay outside

Note: This project is not affiliated with the company Fifth Season which was founded as RoBotany Ltd. It is also not related to several other projects on Github with the repositary name Robotany.

## Parts

* Raspberry Pi Zero W
<img src = "images/rpi_zero.jpg" width = 200>

* SRD-03VDC-SL-C 3V relay board or equivalent
<img src = "images/relays.jpg" width = 200>

* 12V solenoid water valve
<img src = "images/solenoid_water_valve.jpg" width = 200>

* Water hammer arrestor
<img src = "images/water_hammer_arrestor.jpg" width = 200>

* 12V Power supply
<img src = "images/12v_power_supply.jpg" width = 200>

* Length of cable suitable for carrying 12V from where the pi will be located to the solendoid valve
<img src = "images/12v_cable.jpg" width = 200>

* Weather resistant mains power outlet with at least two outlets
<img src = "images/power_outlet.jpg" width = 200>

* Wall box for power outlet above 
<img src = "images/wall_box.jpg" width = 200>

* Mains cable and plug suitable for use outdoors
<img src = "images/extension_chord.jpg" width = 200>

* Outdoor weatherproof Enclosure
<img src = "images/enclosure.jpg" width = 200>

* Fittings to connect solenoid valve and water hammer arrestor to your garden faucet and hospipe.

## Important steps

### Install Raspian onto SD Card
1. Dowload Raspberry Pi Imager from https://www.raspberrypi.org/downloads/
2. Launch Raspberry Pi Imager and follow instructions to install Raspian on an SD card

### Set up Raspberry Pi Zero W
Install SD card with Raspian into Pi, connect mouse, keyboard and monitor and power. Follow instructions to select language, keyboard layout and timezone.

### Set Static IP Address
Note: I still haven't got this to work yet, Was folllowing a combination of instructions from these two links:
https://www.raspberrypi.org/forums/viewtopic.php?p=1500626
https://howtoraspberrypi.com/how-to-raspberry-pi-headless-setup/

### Enable VNC server
1. Open command prompt
2. Type **sudo raspi-config**
3. Go to "Interfacing Options" then "VNC" and select the option to enable the VNC server.
4. Exit the configuration menu

### Connect to VNC Server
1. Obtain IP address from Raspberry Pi by typing **ifconfig wlan0** (or **ifconfig eth0** if connected to the network via ethernet).
2. Install a VNC client on your other device and use the IP address from above, username and password. (Default username = pi, password = raspberry). A VNC viewer can be dowloaded from here: https://www.realvnc.com/en/connect/download/viewer/

### Decide which pins to use
Type **pinout** in a terminal window to get a handy diagram. You'll need:
* A 3.3V pin
* A ground pin
* Any other GPIO pin for the signal to the relay

Read https://www.raspberrypi.org/documentation/usage/gpio for more information about pins.

### Install required packages
From the command line run the following commands to install the packages required:

sudo apt-get update
sudo apt-get install rpi.gpio

### Write/Install Python Code to Control Relay
At a minimum it should contain these commands (I used pin 8):

Set up the pin:
* import RPi.GPIO as GPIO
* GPIO.setmode(GPIO.BOARD)
* GPIO.setup(8, GPIO.OUT)

Turn pin on and off:
* GPIO.output(8, True)
* GPIO.output(8, False)

### Set up Pi to Run Script on Bootup
Haven't figured out how to do this yet.

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

### Connect Solenoid Valve and Water Hammer Arrestor to Garden Faucet/Hose System
You'll probably need a trip to your favourite hardware store to find the right combination of adaptors and fittings. It's not pretty!
