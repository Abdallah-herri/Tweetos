# -*- coding: utf-8 -*-

# it's impossible to store directly instance of class in MongoDB
# so we need tp transform instances of class to dictionary (recursively)
def normalize(var):
	if hasattr(var, '__dict__') or isinstance(var, dict): # if var is an instance of class or dictionary
		result = {}
		# if var is an instance of class, we need to convert it to dictionary else var is already dictionary
		obj = var.__dict__ if hasattr(var, '__dict__') else var
		
		# for each attributes of instance of var
		for (key, value) in obj.items():
			result[key] = normalize(value) # normaize each values
	elif isinstance(var, list): # if var is an ArrayList
		result = []
		# normalize all elements in the ArrayList
		for value in var:
			result.append(normalize(value))
	else: # if var isn't an instance of class or an ArrayList, then we return it
		result = var
	
	return result
