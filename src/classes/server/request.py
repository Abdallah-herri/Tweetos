# -*- coding: utf-8 -*-

class Request:
	__GET = None
	__POST = None

	def __init__(self, data):
		self.data = {}
		#parse data to associate key and value
		for arg in data:
			t = arg.split('=')
			if len(t) > 1 : self.data[t[0]] = t[1]

	# get all values
	def getAll(self):
		return self.data

	# get value by key
	def get(self, query):
		return self.getAll()[query]

	# test if key exist
	def isset(self, query):
		return (query in self.getAll())

	# Request._GET() is equivalent to $_GET in php (but it isn't an array, it's an object : so call the method at the top if you want to use it)
	@staticmethod
	def _GET():
		if Request.__GET is None:
			# create object one time (singleton)
			from classes.server.get import RequestGET
			Request.__GET = RequestGET()

		return Request.__GET

	# Request._POST() is equivalent to $_POST in php (but it isn't an array, it's an object : so call the method at the top if you want to use it)
	@staticmethod
	def _POST():
		if Request.__POST is None:
			# create object one time (singleton)
			from classes.server.post import RequestPOST
			Request.__POST = RequestPOST()

		return Request.__POST

