from pprint import pprint
from includes.geoname import geoname

def filter_results(obj, results):

	query = {}

	for res in results:
		res["hierarchy"] =[]
		query["geonameId"] = res["geonameId"]
		request = geoname("hierarchyJSON" , query)
		name = ''
		for ac in request:

			if(ac["fcode"] == "AREA" or ac["fcode"] == "CONT" ):
				continue

			if(ac["name"] == name):
				res["hierarchy"][-1] = ac
			else:
				res["hierarchy"].append(ac)
		
			name = ac["name"]


	exclu = []

	for i in results:
		for j in results:
			verif = True

			if(i == j or len(j["hierarchy"])>=len(i["hierarchy"])): 
				continue

			for place in range(0,len(j["hierarchy"])):
				if(i["hierarchy"][place]["name"] != j["hierarchy"][place]["name"]):
					verif = False
				
			if (verif):
				exclu.append(j["name"])

	count = len(results)
	
	for e in exclu:
		j = 0
		
		while j < count:
			a = results[j]["name"]
			
			if (e == a):
				results.pop(j)
				count -= 1
			else:
				j += 1

