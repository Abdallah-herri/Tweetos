from classes.server.request import Request
from classes.twitter.tweetos import Tweetos


class Page:
	@staticmethod
	def action():
		r = {success:False}
		avi = Request._GET()
		id_tweet = avi.get("id_tweet")
		index = avi.get("index")
		vote =avi.get("vote")
		tweet = Tweetos.collection.find({"_id" : id_tweet)})
		good = tweet.place[index].good
		bad = tweet.place[index].bad
		good_index = "place." + index + ".good"
		bad_index = "place." + index + ".bad"

		if (tweet is None):
			return r

		if (len(tweet.place) < int(index)):
			return r

		if (vote == "1"):
			good +=1

		else:	
			bad+=1

		Tweetos.collection.update_one(
	        {"id" : id_tweet},
	        {"$set": 
	        	{
	          		good_index : good,
	          		bad_index : bad
	       		}
        	}
        )

    	r.success = True
    	return r
