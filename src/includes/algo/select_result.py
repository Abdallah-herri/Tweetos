from includes.algo.filter_text import filter_text

def select_result(obj, places, array):
	text = filter_text(obj.text)
	lMax = 0
	temp = []
	
	for p in places:
		place_name = p["name"]
		splitted = place_name.split(' ')
		length = len(splitted)
		
		if place_name in text:
			temp.append(p)
			if length > lMax:
				lMax = length
	
	for p in temp:
		place_name = p["name"]
		splitted = place_name.split(' ')
		length = len(splitted)
		
		if length == lMax:
			array.append(p)
	
	return lMax
