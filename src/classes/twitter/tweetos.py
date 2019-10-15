# -*- coding: utf-8 -*-

from pymongo import MongoClient
from classes.twitter.connexion import TweetosAPI

# class wich manage tweet
# all classe which will need to collect tweets will have to expand (extend) this class. These classes are in api folder
class Tweetos:
	#all static vars :

	# twitter tokens (oauth authentification)
	__KEY    = 'npwSpJSxDOx3NPZEH9ImbjTjj'
	__SKEY   = 'orqNaqqWc0WogvmoK4fHVy8JEL7q7HcmADxqlugyodfEKhNhU5'
	__TOKEN  = '956614147491467264-u2Ldje59LhlwKNxvaKlybJD12LgSCik'
	__STOKEN = 'dTQ8veqLa3mBL8z0CZ6y84Tl2upYh7qOOyrhsUHQFQ2jL'
	
	# twitter connexion (look connexion.py)
	connexion = None
	
	# MongoDB :
	# db (contains the collections)
	db = MongoClient()["tweetos"]
	# collection which contains all tweets
	collection = db["tweet"]

	def __init__(self):
		# we make only once authentication to twitter (singleton)
		if Tweetos.connexion == None:
			Tweetos.connexion = TweetosAPI(Tweetos.__KEY, Tweetos.__SKEY, Tweetos.__TOKEN, Tweetos.__STOKEN)

		# attribute which will contains tweets that we will have collected
		self.data = []
		
