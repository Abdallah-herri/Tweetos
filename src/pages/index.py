# -*- coding: utf-8 -*-

from tweepy import TweepError
from bson.json_util import dumps
from classes.modeles.tweet import Tweet
from classes.twitter.tweetos import Tweetos
from classes.twitter.api.user import TweetosUser
from classes.server.request import Request

class Page:
	@staticmethod
	def action(template):
		# if user submit to extract these tweets
		is_posted = Request._POST().isset("submit")
		# if display success or error message
		is_success = True
		
		if is_posted and Request._POST().isset("name"):
			try:
				# request to twitter to collect tweet
				response = TweetosUser(Request._POST().get("name")).data
				# store all tweets that we have collected
				Tweet.storeList(response)
			except TweepError:
				# error
				is_success = False
		
		# collect all tweets in db
		data = Tweetos.collection.find({"place":{"$ne":None}})
		
		# generate render of the template and sending data to the template
		render = template.render({
			"tweets":dumps(data),
			"is_posted":is_posted,
			"is_success":is_success
		})
		
		return render
		
