# -*- coding: utf-8 -*-

from classes.modeles.geo import Geolocalisation

# this class represent a place (like a city, country, place...)
class Place(Geolocalisation):
	def __init__(self, obj):
		super(Place, self).__init__(Geolocalisation.PLACE)

		# all info of the place
		self.name = obj["name"]
		self.country = obj["country"]
		self.country_code = obj["country_code"]
		self.place_type = obj["place_type"]
