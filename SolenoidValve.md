[Return to Readme](README.md)

# Control a Solenoid Valve

This section tells you how to open and close a solenoid valve. This valve can be attached to the mains or a water pump (with proper design considerations to prevent damabging the pump).

## Parts

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

* Fittings to connect solenoid valve and water hammer arrestor to your garden faucet and hospipe.

## Important Steps

### Decide which pins to use

Type `pinout` in a terminal window to get a handy diagram. You'll need:

* A 3.3V pin
* A ground pin
* Any other GPIO pin for the signal to the relay

Read https://www.raspberrypi.org/documentation/usage/gpio for more information about pins.

### Write/Install Python Code to Control Relay

You can use RobotanyMain.py - it is ready to go, or you can write your own.
At a minimum, the script should contain these commands (in this example I used pin 8):

Set up the pin:

* `import RPi.GPIO as GPIO`
* `GPIO.setmode(GPIO.BOARD)`
* `GPIO.setup(8, GPIO.OUT)`

Turn pin on and off:

* `GPIO.output(8, True)`
* `GPIO.output(8, False)`

### Connect Solenoid Valve and Water Hammer Arrestor to Garden Faucet/Hose System

You'll probably need a trip to your favourite hardware store to find the right combination of adaptors and fittings. It's not pretty!


[Return to Readme](README.md)
