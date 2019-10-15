#!/usr/bin/env python3
# -*- coding: utf-8; -*-

# cgi and display errors
import cgitb
cgitb.enable()

# import us sources and libraries
import sys
sys.path.insert(0, "./src")
sys.path.insert(0, "./libraries")

#imports python modules
import os
import importlib

os.environ["NLTK_DATA"] = "./data"

# data dir (it's used for nltk)
import nltk
nltk.data.path.append("./data/nltk_data")

# imports libraries
from jinja2 import Environment, FileSystemLoader

# imports us sources
from classes.server.request import Request
from includes.enc_print import enc_print

# headers
enc_print("Content-type: text/html; charset=utf-8")
enc_print("")

i = 0
find = False
is_json = Request._GET().isset("json")
all_pages = os.listdir("./src/pages/json") if is_json else os.listdir("./src/pages")
# page name
page = Request._GET().get("p") if Request._GET().isset("p") else "index"

# test if page exist
while i < len(all_pages) and not find:
	file = all_pages[i]
	if file.endswith(".py") and file[:-3] == page:
		find = True
	i += 1

if not find :
	print("404 not found")
	sys.exit(1)


if is_json :
	import json

	action = importlib.import_module("pages.json." + page)
	# run page
	render = action.Page.action()

	enc_print(json.dumps(render))
else :
	# open template
	import codecs
	
	template_dir = "./template"
	template_file = codecs.open(template_dir + "/" + page + ".html", "r", "utf8")
	template = Environment(loader=FileSystemLoader(template_dir)).from_string(template_file.read())
	template_file.close()
	
	# import page file
	action = importlib.import_module("pages." + page)

	# run page
	render = action.Page.action(template)
	enc_print(render)
