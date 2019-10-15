# -*- coding: utf-8 -*-

from classes.modeles.tweet import Tweet
from classes.modeles.coord import Coord
from classes.modeles.geo import Geolocalisation
from classes.modeles.geo_routines.place import Place
from classes.modeles.geo_routines.position import Position
from classes.modeles.geo_routines.estimation import Estimation

class TweetFromMongo(Tweet):
	def __init__(self, data):
		# super constructor
		super(TweetFromMongo, self).__init__(
			id = data["id"],
			date = data["date"],
			entities = data["entities"],
			lang = data["lang"],
			text = data["text"],
			userid = data["userid"],
			username = data["username"]
		)
		
		array_place = data["place"]
		
		for place in array_place:
			# if place is not None, we will associate an instance of Geolocalisation for place attribute
			if place != None:
				if place["type"] == Geolocalisation.POSITION: # if tweet is geolocalized with a precise position
					p = Position()
				elif place["type"] == Geolocalisation.PLACE: # else it is a simple place
					p = Place(place)
				else:
					p = Estimation(place["name"], place["precision"], place["good"], place["good"])
				
				# add coordinates to the place
				for coord in place["coordinates"]:
					p.addCoord(Coord(coord.lat, coord.lng))
				
				self.place.append(p)
