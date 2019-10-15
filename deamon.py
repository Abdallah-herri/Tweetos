#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "./src")
sys.path.insert(0, "./libraries")

#nltk lib
import os
import nltk
os.environ["NLTK_DATA"] = "./data"
nltk.data.path.append("./data/nltk_data")

from classes.twitter.api.stream import TweetosStream

keyword_list=["move", "at", "in", "to"]

listener = TweetosStream()
listener.stream.filter(track=keyword_list, languages=["en"])
#listener.stream.filter(locations=[-180,-90,180,90])