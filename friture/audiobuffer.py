#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2009 Timothée Lecomte

# This file is part of Friture.
#
# Friture is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as published by
# the Free Software Foundation.
#
# Friture is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Friture.  If not, see <http://www.gnu.org/licenses/>.

from friture.ringbuffer import RingBuffer

FRAMES_PER_BUFFER = 1024

class AudioBuffer():
	def __init__(self):
		self.ringbuffer = RingBuffer()
		self.newpoints = 0

	def data(self, length):
		return self.ringbuffer.data(length)

	def newdata(self):
		return self.data(self.newpoints)

	def set_newdata(self, newpoints):
		self.newpoints = newpoints
