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

class Coordinate:
	def __init__(self, rawlat, rawlong):
		self.lat = rawlat / 100000.0
		self.long = rawlong / 100000.0

	def __str__(self):
		if self.lat >= 0:
			dirlat = 'N'
		else:
			dirlat = 'S'
		if self.long >= 0:
			dirlong = 'E'
		else:
			dirlong = 'W'
		return "[%c %f, %c %f]" % (dirlat, abs(self.lat),
			dirlong, abs(self.long))

	def toGPX(self):
		return 'lat="%f" lon="%f"' % (self.lat, self.long)
