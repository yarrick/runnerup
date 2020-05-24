
Readme file for runnerup (GH-601 transfer utility)

http://code.kryo.se/runnerup/


How to install:

1. Install the USB-serial driver (Prolific PL-2303)
   Windows users: From the GH-601 CD or google it
   Linux users: modules usbserial and pl2303
2. Install Python (2.6 is known to work)
3. Install pySerial
4. Windows users must install pyWin32
5. Done!


How to use:

1. On the GPS, go to CONFIGURATION, and then choose UPLOAD TO PC
2. Connect the USB cable to the GPS and the computer
3. Run python runnerup.py <PORT>
   where <PORT> is your com port, (Usually /dev/ttyUSB0 on Linux)
4. GPS should say "Waypoint/Training Data Send O.K."
5. All your waypoints/tracks should be printed on the screen in
   GPX format


Stuff left to do:
- CSV output
- KML/Google Earth output
- HTML/Google Maps output
- Calculating avg. speed of a run


Get the latest version at:
http://github.com/yarrick/runnerup


runnerup - GH-601 transfer utility
Copyright (C) 2009 Erik Ekman

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
