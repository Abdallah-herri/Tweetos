# -*- coding: utf-8 -*-

import sys
from classes.server.request import Request

class RequestPOST(Request):
	def __init__(self):
		super(RequestPOST, self).__init__(sys.stdin.read().split('&'))
