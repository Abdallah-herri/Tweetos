from includes.algo.parse_text import parse_text
from includes.algo.select_result import select_result
from includes.algo.filter_requests import filter_requests
from includes.algo.filter_elements import filter_elements
from includes.algo.filter_results import filter_results
from includes.algo.group_results import group_results
from includes.geoname import geoname
from pprint import pprint

def algo(obj):
	# NLTK part
	tags = parse_text(obj.text) # [(word1, tag), (word2, tag)....] -> tokeniser (2 : UML activity)
	# GeoName part
	requests = {} # results of requests from geoname
	query = {"maxRows": 20}

	results = [] # result of the algo which will be returned

	# find words which could be interesting (3 : UML activity)
	# make requests (4 : UML activity)
	for e in tags:
		placename = e[0]
		query["q"] = placename
		r = geoname("searchJSON", query)
		requests[placename] = {"count": 0, "results": []}
		
		# select_result (7: UML activity) :
		# select results which are included in sentence
		# and select results with the mosts occurences (number of words)
		count = select_result(obj, r, requests[placename]["results"])
		requests[placename]["count"] = count
	
	filter_requests(obj, requests, results)
	
	filter_elements(obj, results)
	
	filter_results(obj, results)
	
	group_results(obj, results)
	
	return results
