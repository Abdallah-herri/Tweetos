# -*- coding: utf-8 -*-

from classes.modeles.geo import Geolocalisation

# this class represent an estimation
class Estimation(Geolocalisation):
	def __init__(self, name, precision, good, bad):
		super(Estimation, self).__init__(Geolocalisation.ESTIMATION)

		# all info of the estimation
		self.name = name
		self.precision = precision
		self.good = good
		self.bad = bad

