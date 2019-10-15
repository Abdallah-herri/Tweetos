# -*- coding: utf-8 -*-

import nltk
from includes.geoname import geoname

class Page:
	@staticmethod
	def action(template):
		sentence = "U r nice @"
		tokens = nltk.word_tokenize(sentence)
		tagged = nltk.pos_tag(tokens)
		tree = nltk.chunk.ne_chunk(tagged)
		#tree = []
		
		test = geoname("searchJSON", {"q": "comedie"})
		
		return (template.render({
			"sentence": sentence,
			"tokens":tokens,
			"tagged":tagged,
			"tree":tree,
			"ok": {"a":1, "b":2, "c": 3},
			"ok2": test
		}))
		
