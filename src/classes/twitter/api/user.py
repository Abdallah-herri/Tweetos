# -*- coding: utf-8 -*-

from classes.twitter.tweetos import Tweetos
from classes.modeles.tweet import Tweet
from classes.modeles.tweet_routines.from_twitter import TweetFromTwitter

# class to get tweet of an user
class TweetosUser(Tweetos):
	count = 10

	def __init__(self, user):
		# call the constructor of super class (Tweetos)
		super(TweetosUser, self).__init__()
		# request to twitter
		response = Tweetos.connexion.api.user_timeline(screen_name = user, count = TweetosUser.count, include_rts = True)
		# we made tweets objects (modele) from the response that we stock in data attribute
		Tweet.instantiateList(TweetFromTwitter, response, self.data)
