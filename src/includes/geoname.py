import requests
from includes.algo.filter_text import filter_text

'''
libraries :
- searchJSON (http://www.geonames.org/export/geonames-search.html)
- http://www.geonames.org/export/web-services.html
'''

def geoname(library, query):
	url = "http://api.geonames.org/"
	
	query["username"] = "tweetos"
	query["charset"] = "UTF8"
	
	json = requests.get(url + library, params=query)
	request = json.json()
	results = []
	
	for e in request["geonames"]:
		if ("adminCode1" not in e) or ("fcode" not in e):
			continue
		
		obj = {}
		obj["geonameId"] = e["geonameId"]
		obj["name"] = filter_text(e["toponymName"])
		obj["hierarchy"] = []
		obj["fcode"] = e["fcode"]
		obj["fcl"] = e["fcl"]
		obj["lat"] = e["lat"]
		obj["lng"] = e["lng"]
		obj["admin_code"] = e["adminCode1"]
		
		results.append(obj)
	
	return results
