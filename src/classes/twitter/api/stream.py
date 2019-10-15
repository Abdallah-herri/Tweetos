# -*- coding: utf-8 -*-

from classes.twitter.tweetos import Tweetos
from classes.modeles.tweet_routines.from_twitter import TweetFromTwitter
import json
import tweepy

# class to get tweet of an user
class TweetosStream(Tweetos, tweepy.StreamListener):
	def __init__(self):
		# call the constructor of super class Tweetos
		Tweetos.__init__(self)
		# call constructor of super class StreamListener
		tweepy.StreamListener.__init__(self, api=tweepy.API(wait_on_rate_limit=True))
		# stream attribute can be used to apply many methods (look tweepy doc)
		self.stream = tweepy.Stream(auth=Tweetos.connexion.auth, listener=self)
	
	# for each tweet that we receive, this method is called automatically
	# data is the tweet object at json format
	def on_data(self, data):
		# parse json
		datajson = json.loads(data)
		instance = TweetFromTwitter(datajson)
		
		if len(instance.place) > 0:
			print("Ajout d'un tweet")
			instance.store()
