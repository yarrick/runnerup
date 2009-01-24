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
import sys
import datetime
from coord import *

class Track:
	def __init__(self, date, length, duration, coords):
		self.date = date
		self.length = length
		self.duration = duration / 10.0
		self.coords = coords
	
	def __str__(self):
		coordstr = ' '.join(map(str, self.coords))
		return "Track %s, %d meters, %d seconds, path: %s" % (self.date,
			self.length, self.duration, coordstr)
	
	def getName(self):
		return '  <name>Track from %s</name>' % self.date

	def getDesc(self):
		return '  <desc>Length %d meters</desc>' % self.length

	def getComment(self):
		return '  <cmt>Duration %d seconds</cmt>' % self.duration

	def coordToGpxTrkseg(self, coord):
		return '  <trkseg>\n    <trkpt %s></trkpt>\n  </trkseg>' % \
			coord.toGPX()

	def toGPX(self):
		return '<trk>\n%s\n%s\n%s\n%s\n</trk>' % (self.getName(), 
			self.getDesc(), self.getComment(), 
			'\n'.join(map(self.coordToGpxTrkseg, 
			self.coords)))

class TrackReader:
	cmd_get_tracks =      0x80
	cmd_get_more_tracks = 0x81
	empty_msg_length = 18

	def __init__(self, comm):
		self.comm = comm

	def read(self):
		self.comm.sendCommand(self.cmd_get_tracks)
		data = self.comm.readReply()
		tracks = []
		while len(data) > self.empty_msg_length:
			tracks.append(self.parseTrack(data))
			self.comm.sendCommand(self.cmd_get_more_tracks)
			data = self.comm.readReply()
		return tracks

	def parseTrack(self, data):
		trdata = struct.unpack(">BBBBBBIIhh", data[:18])
		date = datetime.datetime(trdata[0] + 2000, trdata[1],
			trdata[2], trdata[3], trdata[4], trdata[5])
		duration = trdata[6]
		length = trdata[7]
		data = data[18:]
		coords = []
		while len(data) > 0:
			lldata = struct.unpack(">ii", data[:8])
			coords.append(Coordinate(lldata[0], lldata[1]))
			data = data[8:]
		return Track(date, length, duration, coords)

