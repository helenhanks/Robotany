# Robotany
Automated Gardening System

## Parts

* Raspberry Pi Zero W
* SRD-03VDC-SL-C 3V relay or equivalent
* 12V solenoid water valve
* 12V Power supply
* Mains power socket or extension lead
* Project box

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

### Assemble Power System
Diagram to follow. Refer to https://www.circuitbasics.com/setting-up-a-5V-relay-on-the-arduino/ for a rough idea.

### Decide which pins to use
Type **pinout** in a terminal window to get a handy diagram. You'll need:
* A 3.3V pin
* A ground pin
* Any other GPIO pin for the signal to the relay
Read https://www.raspberrypi.org/documentation/usage/gpio for more information about pins.

### Write Python Code to Control Relay
At a minimum it should contain these commands (I used pin 8):

Set up the pin:
* import RPi.GPIO as GPIO
* GPIO.setmode(GPIO.BOARD)
* GPIO.setup(8, GPIO.OUT)

Turn pin on and off:
* GPIO.output(8, True)
* GPIO.output(8, False)


