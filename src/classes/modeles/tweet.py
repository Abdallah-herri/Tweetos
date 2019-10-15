# -*- coding: utf-8 -*-

from classes.twitter.tweetos import Tweetos
from includes.mongo_normalize import normalize

# our tweet modele
class Tweet(object):
	def __init__(self, id, date, entities, lang, text, userid, username):
		# all attributes of a twitter object
		self.id = id
		self.date = date
		self.entities = entities
		self.lang = lang
		self.text = text
		self.userid = userid
		self.username = username
		self.place = []
		
	# store this tweet in our DB (if single = true, we check if the tweet isn't in the db)
	def store(self, single=True):
		find = Tweetos.collection.find({"id": self.id})
		if find.count() > 0 and single:
			return
		
		# insert the current object in DB (before we convert this object to dictionary with normalize)
		Tweetos.collection.insert(normalize(self))

	# use this method to avoid to repeat the "for" everytime that you need to store tweets in DB
	# if single = true, we check if  for each tweet it isn't in db 
	@staticmethod
	def storeList(array, single=True):
		for item in array:
			item.store(single)
			
	# use this method to avoid to repeat the "for" everytime that you need to store tweets (collected from tweepy) in list
	# if you want to instatiate the list with TweetFromTwitter, then you need to give TweetFromTwitter for tweet_class parameter
	# if you want to instatiate the list with TweetFromMongo, then you need to give TweetFromMongo for tweet_class parameter
	@staticmethod
	def instantiateList(tweet_class, array, result):
		for item in array:
			result.append(tweet_class(item))
