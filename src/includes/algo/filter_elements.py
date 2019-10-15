def filter_elements(obj, results):
	count = len(results)
	i = 0
	
	while (i < count):
		a = results[i]
		j = 0
		
		while j < count:
			b = results[j]
			
			if (i != j) and (a["name"] == b["name"]) and (a["admin_code"] == b["admin_code"]) and (a["fcl"] <= b["fcl"]):
				results.pop(j)
				count -= 1
				
				if (i > j):
					i -= 1
			else:
				j += 1
		
		i += 1
