$().ready(function() {
	if ($("section#index").length !== 1) {
		return;
	}
	
	// create map
	var mymap = new LeafLetMap("map");
	// div which contain json of all tweets
	var tweets_elements = $("div#tweets");
	// parse json
	var tweets = JSON.parse(tweets_elements.html());

	// we display the tweet on map
	for (var i in tweets) 
	{
		var item = tweets[i];
		for (var j in item.place) 
		{
			var place = item.place[j];
			mymap.addMarker(place, item);
		}
	}
	
	mymap.displayMarker();
});
