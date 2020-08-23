[Return to Readme](README.md)

# Setting up a New Raspberry Pi

## Parts

* Raspberry Pi Zero W
<img src = "images/rpi_zero.jpg" width = 200>

## Important Steps

### Install Raspian onto SD Card

1. Download Raspberry Pi Imager from https://www.raspberrypi.org/downloads/
2. Launch Raspberry Pi Imager and follow instructions to install Raspian on an SD card

### Set up Raspberry Pi Zero W

1. Install SD card with Raspian into Pi
2. Connect mouse, keyboard, monitor, and power. 
3. Follow instructions to select language, keyboard layout, and timezone.

### Give Pi a Recognisable Name to Find it Easily on the Network

1. Use `sudo raspi-config` to change the settings of the pi.
2. Choose '2. Network Options'
3. Choose 'N1 Hostname'
4. Choose 'OK'
5. Type in Hostname you want and choose 'OK'
6. Choose 'Finish'
7. You may be prompted to restart your Pi.

### Enable VNC server

1. Open command prompt
2. Type `sudo raspi-config`
3. Go to "Interfacing Options" then "VNC" and select the option to enable the VNC server.
4. Exit the configuration menu

### Connect to VNC Server

1. Install a VNC client on your other device and use the hostname from above, username and password. (Default username = pi, password = raspberry). A VNC viewer can be dowloaded from here: https://www.realvnc.com/en/connect/download/viewer/
2. Alternatively, you can obtain the IP address from Raspberry Pi by typing **ifconfig wlan0** (or **ifconfig eth0** if connected to the network via ethernet).

[Return to Readme](README.md)
