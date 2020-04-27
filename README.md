# Robotany
Automated Gardening System

## Parts

* Raspberry Pi Zero W
* 12V solenoid water valve
* 12V Power supply
* Project box

## Important steps

### Install Raspian
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


