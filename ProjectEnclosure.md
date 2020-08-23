[Return to Readme](README.md)

# Install Pi and Related Components in a Weatherproof Project Enclosure

## Parts

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

[Return to Readme](README.md)
