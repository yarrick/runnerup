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

import serial
import sys
import struct

class GH60xDataError:
	def __init__(self, msg):
		pass

class GH60xNotConnectedError:
	pass

class GH60xSerial:
	def __init__(self):
		self.conn = None
	
	def __del__(self):
		if self.conn != None:
			self.conn.close()
	
	def connect(self, port, speed):
		self.conn = serial.Serial(
			port=port,
			baudrate = speed,
			timeout = 10)

	def checksum(self, data):
		return reduce(lambda a, b: a ^ b, map(ord, data))
	
	def sendCommand(self, command):
		if self.conn == None:
			raise GH60xNotConnectedError()
		print >> sys.stderr, "Writing...",
		strs = [ '\x02', '\x00\x01' ]
		strs.append(chr(command & 0xff))
		strs.append(chr(self.checksum(''.join(strs[1:]))))
		msg = ''.join(strs)
		self.conn.write(msg)
		print >> sys.stderr, "%d bytes" % len(msg)

	def readReply(self):
		if self.conn == None:
			raise GH60xNotConnectedError()
		print >> sys.stderr, "Reading...",
		header = self.conn.read(3)
		if len(header) < 3:
			print >> sys.stderr, "\nNo reply from device."
			print >> sys.stderr, "Put GPS in 'Upload to PC' mode"
			sys.exit(0)

		hdrdata = struct.unpack(">xH", header)
		length = hdrdata[0]
		data = self.conn.read(length + 1)
		if len(data) != length + 1:
			raise GH60xDataError("Could not read all data")
		print >> sys.stderr, "%d bytes" % length
		given_chksum = ord(data[length])
		chksum = self.checksum(header[1:])
		data = data[:-1]
		chksum ^= self.checksum(data)
		if given_chksum != chksum:
			print >> sys.stderr, \
				"Invalid checksum! Was %02X, should be %02X" \
				% (chksum, given_chksum)
		return data

