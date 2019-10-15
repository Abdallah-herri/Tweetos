import nltk
from includes.algo.pattern_matcher import pattern_matcher
from includes.algo.filter_text import filter_text

def parse_text(text):
	tags = nltk.pos_tag(nltk.word_tokenize(text)) # [(word1, tag), (word2, tag)....] -> tokeniser (2 : UML activity)
	
	for i in range(0, len(tags), 1):
		tags[i] = (filter_text(tags[i][0]), tags[i][1])
	
	result = []
	tags = pattern_matcher(tags)
	accept_tags = [
		"NN", # NN -> nom commun
		"NNP", # NNP -> nom propre
		"FW",# FW -> mot étranger
		"GRP"
	] # tags returned by NLTK which could be interesting (http://www.nltk.org/book_1ed/ch05.html)
	
	exclude_words = [
		"http",
		"@",
		"https"
	]
	
	for e in tags:
		if (e[1] in accept_tags) and (e[0] not in exclude_words):
			 result.append(e)
	return result
