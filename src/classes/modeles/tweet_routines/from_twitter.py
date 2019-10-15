# -*- coding: utf-8 -*-

from classes.modeles.tweet import Tweet
from classes.modeles.coord import Coord
from classes.modeles.geo_routines.place import Place
from classes.modeles.geo_routines.position import Position
from classes.modeles.geo_routines.estimation import Estimation
from includes.algo.algo import algo
from includes.stats.precision import precision

# class to import tweet object from request (so TweetFromTwitter extends Tweet)
class TweetFromTwitter(Tweet):
	def __init__(self, data):
		# super constructor
		super(TweetFromTwitter, self).__init__(
			id = str(data["id"]),
			date = data["created_at"],
			entities = data["entities"],
			lang = data["lang"],
			text = data["text"],
			userid = str(data["user"]["id"]),
			username = data["user"]["name"]
		)
		
		# if the tweet is geolocalised by a point or a place or estimated
		if data["coordinates"] != None: # geolocalised by a point
			p = Position()
			p.addCoord(TweetFromTwitter.__createCoord(data["coordinates"]["coordinates"]))
			self.place.append(p)
		elif data["place"] != None: # geolocalised by a place
			p = Place(data["place"])
			coordinates = data["place"]["bounding_box"]["coordinates"][0]
			
			for coord in coordinates:
				p.addCoord(TweetFromTwitter.__createCoord(coord))
			
			self.place.append(p)
		else:
			results = algo(self)
			
			if (len(results) != 0):			
				pr = precision(results)
				
				for e in results:
					p = Estimation(e["name"], pr, 0, 0)
					p.addCoord(Coord(e["lat"], e["lng"]))
					self.place.append(p)
	
	@staticmethod
	def __createCoord(tab):
		lat = tab[1]
		lng = tab[0]
		return Coord(lat, lng)
	
