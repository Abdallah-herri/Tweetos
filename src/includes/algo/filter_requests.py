def filter_requests(obj, requests, results):
	items = requests.items()
	exclude_requests = {}
	
	for key, value in items:
		exclude_requests[key] = False
	
	for key, value in items:
		for place in value["results"]:
			placename = place["name"]
			words = placename.split(" ")
			
			for w in words:
				if (w == key) or (w not in requests):
					continue
				
				if requests[w]["count"] > requests[key]["count"]:
					exclude_requests[key] = True
				elif requests[w]["count"] < requests[key]["count"]:
					exclude_requests[w] = True
				
	for key, value in items:
		if exclude_requests[key]:
			continue
		
		for place in value["results"]:
			results.append(place)
	
