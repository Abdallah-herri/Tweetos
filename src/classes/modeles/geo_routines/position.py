# -*- coding: utf-8 -*-

from classes.modeles.geo import Geolocalisation

# this class represent an exact geolocalisation/position
class Position(Geolocalisation):
	def __init__(self):
		super(Position, self).__init__(Geolocalisation.POSITION)
