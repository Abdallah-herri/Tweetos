# -*- coding: utf-8 -*-

import os
from classes.server.request import Request

class RequestGET(Request):
	def __init__(self):
		super(RequestGET, self).__init__(os.getenv("QUERY_STRING").split('&'))
