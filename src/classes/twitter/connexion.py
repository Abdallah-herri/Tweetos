# -*- coding: utf-8 -*-

import tweepy

class TweetosAPI:
	def __init__(self, key, skey, token, stoken):
		self.auth = tweepy.OAuthHandler(key, skey)
		self.auth.set_access_token(token, stoken)
		# attribute that we will use to make request (look doc of tweepy to find appropriate methods)
		self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())
		
