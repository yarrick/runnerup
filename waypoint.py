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

import struct
from coord import *

class Waypoint:
	def __init__(self, name, altitude, coord):
		self.name = name
		self.alt = altitude
		self.coord = coord
	
	def __str__(self):
		return "Waypoint \"%s\", alt %d m, %s" % (self.name, 
			self.alt, self.coord)

	def toGPX(self):
		return '<wpt %s>\n  <name>%s</name>\n</wpt>' % \
			(self.coord.toGPX(), self.name)
	
class BadDataLength:
	pass

class WaypointReader:
	cmd_get_waypoints = 0x77

	def __init__(self, comm):
		self.comm = comm
	def read(self):
		self.comm.sendCommand(self.cmd_get_waypoints)
		data = self.comm.readReply()
		if len(data) % 18 != 0:
			raise BadDataLength()
		wps = []
		while len(data) > 0:
			wpdata = struct.unpack(
				">7sxHii", data[:18])
			wpname = wpdata[0].split('\x00', 1)[0]
			wpalt = wpdata[1]
			coord = Coordinate(wpdata[2], wpdata[3])
			wps.append(Waypoint(wpname, wpalt, coord))
			data = data[18:]
		return wps

