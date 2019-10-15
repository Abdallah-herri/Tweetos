from classes.server.request import Request
from classes.twitter.tweetos import Tweetos



	avi = Request._GET()
	id_tweet = avi.get("id_tweet")
	index = avi.get("index")
	vote = avi.get("vote")
	tweet = Tweetos.collection.find({"_id" : id_tweet)})


	if( tweet is None)
		return

	if(len(tweet.place) < index)
		return


	
	def add_vote(array)
		Tweetos.collection.update_one(
        {"id": id_tweet},
        {
        "$set": {
          
        }
        }
    )	
