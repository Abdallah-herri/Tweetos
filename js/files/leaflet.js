/* global L */

// leaflet api token
// var leaflet_token = "pk.eyJ1IjoiZy1lcmVteSIsImEiOiJjamQ0dXlrbDQxYjBpMndxajFzcmR4cHFvIn0.4s-pa5Yg4hAtkSvmSNYlaw";

var leaflet_layer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
});

// create map
function LeafLetMap(container) {
	this.map = L.map(container, {
		center: [10.0, 5.0],
		minZoom: 2,
		zoom: 2
	});

	// group markers
	this.marker_cluster = L.markerClusterGroup();

	leaflet_layer.addTo(this.map);
}

// add marker on created map
// when you add marker, it doesn't display, then you need to call displayMarker when you have finished to add all markers
// @param coor : array of coordinates
// @param text : text which will display when user click on marker

LeafLetMap.prototype.addMarker = function(place, item) {
	var coor = place.coords;
	var lat = 0, lng = 0;
	var marker,e,f,bar;
	var cluster = this.marker_cluster;
	var content = "";

	// avg of coordinates (polygone)
	for (var i in coor) {
		lat += Number(coor[i].lat);
		lng += Number(coor[i].lng);
	}

	lat = lat / coor.length;
	lng = lng / coor.length;
	
	e = $('<div class="trans like"></div>');
	f = $('<div class="trans dislike"></div>');
	bar = $('<progress class="percentage" value="50" max="100"></progress>');

	displaybutton("like", function(svg) {
		content = '<div class = "tweet">' + item.text + '</div>';
		content += '<input id="'+ item.id + '" type ="hidden"/>';
		content += '<p><i>localisation : ' + place.name + '</i></p>';
		content += '<div class="buttons">';
		e.append(svg);
		content += e.prop("outerHTML");
		f.append(svg);
		content += f.prop("outerHTML");
		content += bar.prop("outerHTML");
		content += "</div>";

		marker = L.marker([lat, lng]).bindPopup(content);
		// add marker to the group
		cluster.addLayer(marker);
	});
};


// display all markers
LeafLetMap.prototype.displayMarker = function() {
	this.map.addLayer(this.marker_cluster);
};
