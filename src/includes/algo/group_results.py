from pprint import pprint

def group_results(obj, results):
	array = []
	count = len(results)
	
	for i in range(0, count):
		array.append(results.pop())
	
	i = 0
	
	while (i < count):
		# values
		a = array[i]
		a_hierarchy = a["hierarchy"]
		a_count = len(a_hierarchy)
		# iterator
		j = i
		# grouping
		k_min = a_count
		grouping = False
		
		while (j < count):
			if (i == j):
				j += 1
				continue
			
			# values
			b = array[j]
			b_hierarchy = b["hierarchy"]
			b_count = len(b_hierarchy)
			# iterator
			k = 0
			hierarchy_count = a_count if a_count > b_count else b_count
			deleted = False
			
			while (k < hierarchy_count) and (a_hierarchy[k]["name"] == b_hierarchy[k]["name"]):
				deleted = True
				grouping = True
				k += 1
			
			if (deleted):
				k_min = k if k < k_min else k_min
				array.pop(j)
				count -= 1
			else:
				j += 1
		
		if grouping:
			results.append(a_hierarchy[k_min - 1])
		else:
			results.append(a)
		
		i += 1
