var displaybutton;

(function() {
	var cache = {};
	var shift = {};

	function button(file, callback)
	{
		if (cache[file] !== undefined) {
			if (callback) {
				callback(cache[file]);
			}
		}
		else
		{
			if (shift[file] === undefined)
			{
				shift[file] = {
					shift: [],
				};

				d3.xml("pictures/"+file+".svg").mimeType("image/svg+xml").get(function(error, xml) 
				{
			    	var svg = $(xml.documentElement);
			    	var e;

			    	for (var i in shift[file].shift)
			    	{
			    		e = shift[file].shift[i];

				    	if (e.callback)
				    	{
				    		e.callback(svg);
				    	}
			    	}

			    	cache[file] = svg;
			    	delete cache[file];
			  	});
			}

			shift[file].shift.push({
				callback: callback
			});
		}
	}

	displaybutton = button;
})();


