# -*- coding: utf-8 -*-
import os
import codecs

def browse_dir(location, result):
	if (not(os.path.isdir(location))):
		return

	liste = os.listdir(location)

	for f in liste :
		d = location + "/" + f
		if (os.path.isdir(d) and not(os.path.islink(d))):
			browse_dir(d, result)
		else:
			result.append(d)


def catch_files(location, ext, callback):
	array = []
	browse_dir(location, array)

	for filename in array:
		if filename.endswith("." + ext):
			continue

		file = codecs.open(filename, "r", "utf8")
		out = file.read()
		callback(out)
		file.close()
