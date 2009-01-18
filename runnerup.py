#!/usr/bin/python
'''
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
'''

import sys 
from ghserial import *
from waypoint import *
from track import *

if len(sys.argv) != 3:
	print >> sys.stderr, "Use port and type as argument"
	print >> sys.stderr, "port can be /dev/ttyUSB0 or COM2",
	print >> sys.stderr, "or /dev/tty.usbserial or similar"
	print >> sys.stderr, "type can be 'waypoint' or 'track'"
	sys.exit(1)

if not (sys.argv[2] == "waypoint" or sys.argv[2] == "track"):
	print >> sys.stderr, "Bad type. Use 'waypoint' or 'track'"
	sys.exit(1)

type = sys.argv[2]
comm = GH60xSerial()
try:
	print >> sys.stderr, "Opening port %s..." % sys.argv[1],
	comm.connect(sys.argv[1], 4800)
	print >> sys.stderr, "done"
except:
	print >> sys.stderr, "Opening port %s failed" % sys.argv[1]
	sys.exit(1)

if type == "waypoint":
	wpr = WaypointReader(comm)
	print '\n'.join(map(str, wpr.read()))
	sys.exit(0)

if type == "track":
	tr = TrackReader(comm)
	print '\n'.join(map(str, tr.read()))
	sys.exit(0)

