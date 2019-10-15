#!/usr/bin/env python3
# -*- coding: utf-8; -*-

import sys
import os

sys.path.insert(0, "../../")
sys.path.insert(0, "../../../libraries")

import nltk
os.environ["NLTK_DATA"] = "../../../data"
nltk.data.path.append("../../../data/nltk_data")

# pour chaque fichier de test, il doit y avoit le même en-tête de fichier de la ligne 1 à 12
# le reste c'est votre code de test
from includes.algo.algo import algo
from pprint import pprint

class TestTweet:
	def __init__(self, sentence):
		self.text = sentence


sentence = TestTweet("I'm in Place de la comedie ")
result = algo(sentence)
pprint(result)
