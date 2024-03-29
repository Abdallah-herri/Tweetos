# -*- coding: utf-8 -*-

class Geolocalisation(object):
	# all static attributes :

	# type of Geolocalisation :
	
	# precise position
	POSITION = 0
	# simple place (like country, city...)
	PLACE = 1	
	# generated by our algo
	ESTIMATION = 2
	
	# we need to pass the "type of Geolocalisation" at the constructor because we need this information in DB
	def __init__(self, type):
		self.type = type
		self.coords = []

	def addCoord(self, coord):
		self.coords.append(coord)