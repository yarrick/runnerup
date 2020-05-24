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

class GpxExport:
	def __init__(self):
		self.wplist = []
		self.trklist = []

	def setWaypoints(self, wp):
		self.wplist = wp

	def setTracks(self, tr):
		self.trklist = tr

	def toGPX(self):
		strs = [ '<?xml version="1.0" encoding="UTF-8"?>',
		  '<gpx version="1.0"',
		  '    creator="http://code.kryo.se/runnerup"',
		  '    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
		  '    xmlns="http://www.topografix.com/GPX/1/0"',
		  '    xsi:schemaLocation="http://www.topografix.com/GPX/1/0',
		  '        http://www.topografix.com/GPX/1/0/gpx.xsd">']

		map(strs.append, map(lambda a: a.toGPX(), self.wplist))
		map(strs.append, map(lambda a: a.toGPX(), self.trklist))

		strs.append('</gpx>')
		return '\n'.join(strs)
