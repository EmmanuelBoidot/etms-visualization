var mouseLat = 34.5;
var mouseLng = -94.8;
var datetimeformat = d3.time.format("%Y%m%dT%H:%M:%S");
var timeformat = d3.time.format("%H:%M");
var map = L.map('map').setView([34.5, -95],4);
var svg = d3.select(map.getPanes().overlayPane).append("svg");
var g = svg.append("g").attr("class", "leaflet-zoom-hide");
var popupTimer = null;
var spinner_opts = {
  lines: 17, // The number of lines to draw
  length: 29, // The length of each line
  width: 30, // The line thickness
  radius: 15, // The radius of the inner circle
  corners: 1, // Corner roundness (0..1)
  rotate: 0, // The rotation offset
  direction: 1, // 1: clockwise, -1: counterclockwise
  color: '#000', // #rgb or #rrggbb or array of colors
  speed: 1, // Rounds per second
  trail: 50, // Afterglow percentage
  shadow: false, // Whether to render a shadow
  hwaccel: false, // Whether to use hardware acceleration
  className: 'spinner', // The CSS class to assign to the spinner
  zIndex: 2e9, // The z-index (defaults to 2000000000)
  top: '50%', // Top position relative to parent
  left: '50%' // Left position relative to parent
};
var target = document.getElementById('map');
var spinner = new Spinner(spinner_opts).spin(target);
spinner.stop();

L.tileLayer('http://{s}.www.toolserver.org/tiles/bw-mapnik/{z}/{x}/{y}.png', {
// L.tileLayer('http://{s}.www.toolserver.org/tiles/bw-mapnik/{z}/{x}/{y}.png', {
// L.tileLayer('http://{s}.tile.thunderforest.com/transport/{z}/{x}/{y}.png', {
// L.tileLayer('http://{s}.tile.openstreetmap.com/{z}/{x}/{y}.png', {
    // attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
    attribution: '',
    maxZoom: 18
}).addTo(map);

var info_zoom = d3.select("#info_zoom"),
	info_width = d3.select("#info_width"),
	info_height = d3.select("#info_height");
var opacity_val = 1.0;
var map_width, map_height;
var bounds;
refresh_info_panel();

map.scrollWheelZoom.disable();

map.on('zoomstart', function() {
    opacity_val = parseFloat(d3.selectAll('path').style('stroke-opacity'));
    // console.log(opacity_val);
});

map.on('zoomend', function() {
    refresh_info_panel();
    // console.log(opacity_val);
    update_opacity(opacity_val);
});

// map.on('viewreset', function(e) {
// 	spinner.spin(target)
// });

colors = ['red','blue','green','black','orange'];

var searched_flights = [],displayed_flights=[], selected_flight=[];
var selected_flight_index = -1;
var displayed_flights = [];
var flights = [];
var airlines_list = {}, airlines = [];
var ori_dest_list = {}, ori_dest = [];
var selected_ARL={}, selected_OD={};


map.on('click', function(e) {
    // console.log("Lat, Lon : " + e.latlng.lat + ", " + e.latlng.lng);
    mouseLat = e.latlng.lat;
    mouseLng = e.latlng.lng;
    $("#info_mouseLat").html("Lat : "+mouseLat.toFixed(6));
    $("#info_mouseLng").html("Lng : "+mouseLng.toFixed(6));

    // d3.selectAll("#info_selected_flight")
				// 	.style("display","none");
	// selected_flight=[];
});




// init with two flights
d3.json("json/multi_traj_raw2.json", function(error,data){
	if (!error && typeof data !== 'undefined'){

	// me
	searched_flights = {};
	searched_flights.features = data.hits.hits;
	searched_flights.type = "FeatureCollection";
	delete searched_flights._type;
	delete searched_flights._score;
	for (i = 0; i < searched_flights.features.length; i++) { 
	    searched_flights.features[i].type = "Feature";
	    searched_flights.features[i].geometry = sort_geometry(searched_flights.features[i]);
	    // console.log(searched_flights.features[i]._source)
	    // searched_flights.features[i].altitude = searched_flights.features[i]._source.POSITION[0].ALTITUDE;
	    // searched_flights.features[i].groundspeed = searched_flights.features[i]._source.POSITION[0].GROUNDSPEED;
	    delete searched_flights.features[i]._source.LOCATION;
	    delete searched_flights.features[i]._source.POSITION;
	    // searched_flights.features[i].geometry.type = "LineString"
	    searched_flights.features[i].properties = searched_flights.features[i]._source.AIR[0];
	    searched_flights.features[i].metrics = compute_metrics(searched_flights.features[i])
	}
	console.log("start drawing");
	flights = searched_flights;
	draw_flights(searched_flights);
	draw_metrics(searched_flights.features);
	console.log("done drawing");
	}
});

// when the input range changes update the opacity 
d3.select("#nOpacity_value").on("input", function() {
	update_opacity(+this.value);
});
d3.select("#plus-button").on("mousedown", function() {
	val = d3.select("#nOpacity_value").property("value");
	val = val/1000+.01 // corresponds to .01 increase
	update_opacity(val);
});
d3.select("#minus-button").on("mousedown", function() {
	val = d3.select("#nOpacity_value").property("value")/1;
	val = val/1000-.01 // corresponds to .01 decrease
	update_opacity(val);
});

d3.select("#reduce-button").on("mousedown", function() {
	if (d3.selectAll("#info_selected_flight").style("display")=="block"){
		d3.selectAll("#info_selected_flight").style("display","none")
		d3.selectAll("#reduce-button").text("+")
		// selected_flight_index=-1;
		update_opacity();
	} else {
		if (selected_flight_index!=-1){
			d3.selectAll("#info_selected_flight").style("display",null)
			d3.selectAll("#reduce-button").text("-")
			update_opacity(0.02);
		}
	}
});

d3.select("#save").on("click", function(){
	var html = svg.selectAll("g")
	    .html();
	// var html = d3.select("#map").html();
	html = "<svg width='"+d3.select('#map').style('width')+ "' height='"+d3.select('#map').style('height')+"' version='1.1' xmlns='http://www.w3.org/2000/svg'>"+html+"</svg>";

	console.log(html);
	var imgsrc = 'data:image/svg+xml;base64,'+ btoa(html);
	var img = '<img src="'+imgsrc+'">'; 
	d3.select("#svgdataurl").html(img);


	var canvas = document.querySelector("canvas"),
	  context = canvas.getContext("2d");

	var image = new Image;
	image.src = imgsrc;
	image.onload = function() {
	  context.drawImage(image, 0, 0);

	  var canvasdata = canvas.toDataURL("image/png");

	  var pngimg = '<img src="'+canvasdata+'">'; 
		  d3.select("#pngdataurl").html(pngimg);

	  var a = document.createElement("a");
	  a.download = "map.png";
	  a.href = canvasdata;
	  a.click();
	};
});

function sort_geometry(mflight){
	coord = mflight._source.LOCATION[0].coordinates;
	speed = mflight._source.POSITION[0].GROUNDSPEED;
	alt = mflight._source.POSITION[0].ALTITUDE;
	var ts = [], times = [];
	coord.forEach(function(o,i) {
	  ts.push({
	  	coordinates:coord[i], 
	  	groundspeed:speed[i], 
	  	altitude:alt[i], 
	  	time:datetimeformat.parse(mflight._source.AIR[0].POSIT_DATE[i]+"T"+mflight._source.AIR[0].POSIT_TIME[i])})
	});
	ts.sort(function(a,b){return a.time-b.time;});
	coord = [],speed=[],alt=[],times=[];
	ts.forEach(function(o,i){
		coord.push(o.coordinates);
		speed.push(o.groundspeed);
		alt.push(o.altitude);
		times.push(o.time);
	});

	return {coordinates:coord, groundspeed:speed, altitude:alt, times:times, type:"LineString"};
}

// update the elements
function update_opacity(nOpacity) {
	if (!nOpacity){
		visiblePaths = g.selectAll("path").filter(function(d){return d.displayed=='True'})[0];
		nOpacity = d3.max([0.10,10*0.999/visiblePaths.length]);
	}
	if (nOpacity>1){
		nOpacity = nOpacity/1000;
	}
	// adjust the text on the range slider
	d3.select("#nOpacity_text").text(nOpacity.toFixed(3));
	d3.select("#nOpacity_value").property("value", nOpacity*1000);

	// update the paths opacity
	g.selectAll("path")
		.filter(function(d,i){return i!=selected_flight_index;})
		.style("stroke-opacity", nOpacity);
}

function draw_flights(mflights){
	if (mflights !== "undefined" && mflights.features.length>0){
		spinner.spin(target);
		for (i = 0; i < mflights.features.length; i++) { 
			mflights.features[i].type = "Feature";
			mflights.features[i].displayed = "True";
		}

		update_airlines(mflights);
		update_ori_dest(mflights);

		var transform = d3.geo.transform({point: projectPoint}),
	    path = d3.geo.path().projection(transform);

	    g.selectAll("path").remove();

		d3_features = g.selectAll("path")
			.data(mflights.features)
			.enter().append("path");

		d3_features
			.on("mouseenter", function(d) {
				popup_create2(d.properties);reset_popup_timer();
			})
			.on("click", function(d,i) {
				display_flight_info(d,i);
				update_opacity(0.02);
				popup_create2(d.properties);
				popupTimer = setTimeout(fade_out_popup, 10000);
			});




		map.on("viewreset", reset);

		reset();
		spinner.stop();

		// fit the SVG element to leaflet's map layer
		function reset() {

			bounds = path.bounds(mflights);

			var topLeft = bounds[0],
				bottomRight = bounds[1];

			svg .attr("width", bottomRight[0] - topLeft[0])
				.attr("height", bottomRight[1] - topLeft[1])
				.style("left", topLeft[0] + "px")
				.style("top", topLeft[1] + "px");

			g .attr("transform", "translate(" + -topLeft[0] + "," 
			                                  + -topLeft[1] + ")");

			if (opacity_val==1.0){
				opacity_val = d3.max([0.10,10*0.99/d3_features[0].length]);
			}
			// initialize the path data	
			d3_features.attr("d", path)
				.style("fill-opacity", 0.0)
				.style("stroke", function(d){
					return colors[selected_ARL.indexOf(d.properties.ARL_COD)%colors.length];
				})
				.style("stroke-opacity", opacity_val)
				.attr('fill','blue');

			// make selected flight more opaque
			if (selected_flight_index!=-1){
				d3.selectAll('path')
					.filter(function(o,j){
						return j==selected_flight_index;
					})
					.style("stroke-opacity", 1.0)
			}	
			// adjust the text on the range slider
			d3.select("#nOpacity_text").text(opacity_val.toFixed(3));
			d3.select("#nOpacity_value").property("value", opacity_val*1000);
		} 
	} else {
		alert("No flights for the corresponding query");
	}
	set_query_status(0);
	displayed_flights = searched_flights.features//g.selectAll("path")
		.filter(function(d){return d.displayed=="True"});
	d3.select("#info_flights_num").text("#Flights: "+displayed_flights.length);
	d3.select("#info_flights_ARL").text("#Airlines: "+selected_ARL.length);

	// hide the info for the selected flight
	d3.selectAll("#info_selected_flight").style("display","none");
	selected_flight_index = -1;
}


///////////////added by Aude
function getDistanceFromLatLonInNm(lat1,lon1,lat2,lon2) {
  var R = 6371*0.53996; // Radius of the earth in NM
  var dLat = deg2rad(lat2-lat1);  // deg2rad below
  var dLon = deg2rad(lon2-lon1); 
  var a = 
    Math.sin(dLat/2) * Math.sin(dLat/2) +
    Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
    Math.sin(dLon/2) * Math.sin(dLon/2)
    ; 
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
  var d = R * c; // Distance in km
  return d;
}

function deg2rad(deg) {
  return deg * (Math.PI/180)
}
//////////////////////////////////

function display_flight_info(d,i){
	selected_flight = d;
	selected_flight_index = i;

	info = d3.selectAll("#info_selected_flight");

	info.select("#sel_flight_ori_dest").text(d.properties.DEPT_APRT + " -> " + d.properties.ARR_APRT);
	info.select("#sel_flight_ARL_and_num").text(d.properties.ARL_COD + d.properties.FLI_NUM);
	info.select("#sel_flight_date").text("Date: "+d.properties.ORIG_DATE);
	info.select("#sel_flight_tail").text("Tail: "+d.properties.BEACON_CODE);
	info.select("#sel_flight_aircraft").text("Aircraft: ");
	info.select("#sel_flight_time_ori_exp").text("Departure time (exp): "+"xxxx");
	info.select("#sel_flight_time_ori_act").text("Departure time (act): "+d.properties.ORIG_TIME);	
	info.select("#sel_flight_time_dest_exp").text("Arrival time (exp): "+d.properties.ARR_EST_TIME);
	info.select("#sel_flight_time_dest_act").text("Arrival time (act): "+timeformat(d3.max(d.geometry.times)));	
	info.select("#sel_flight_speed").text("Speed: ")
	info.select("#sel_flight_fuel").text("Fuel: ")
	info.select("#sel_flight_passengers_num").text("#Passengers: ")
	info.select("#sel_flight_passengers_corres").text("#Correspondances: ")

	d3.selectAll('path')
		.filter(function(o,j){
			return j==i;
		})
		.style("stroke-opacity", 1);
	plot_altitude(d);
	plot_groundspeed(d);
	info.style("display",null);
	compute_metrics(d)
}
	
function compute_metrics(d){
	// find the 40NM and 100Nm points from the departure and arrival apts
	//initialize
	depapt_latlon=d.geometry.coordinates[0];
	arrapt_latlon=d.geometry.coordinates[d.geometry.coordinates.length-1];
	apt2apt_dist=getDistanceFromLatLonInNm(depapt_latlon[0],depapt_latlon[1],arrapt_latlon[0],arrapt_latlon[1]);
	if (apt2apt_dist>100){
		pt40dep=d.geometry.coordinates[1]; i40dep=1;
		while (getDistanceFromLatLonInNm(depapt_latlon[0],depapt_latlon[1],pt40dep[0],pt40dep[1])<40)
			{i40dep=i40dep+1;
			pt40dep=d.geometry.coordinates[i40dep];}

		// console.log(d.geometry.coordinates)
		pt100dep=d.geometry.coordinates[1]; i100dep=1;
		while (getDistanceFromLatLonInNm(depapt_latlon[0],depapt_latlon[1],pt100dep[0],pt100dep[1])<100)
			{i100dep=i100dep+1;
			pt100dep=d.geometry.coordinates[i100dep];}
		
		pt40arr=d.geometry.coordinates[d.geometry.coordinates.length-2]; i40arr=d.geometry.coordinates.length-2;
		while (getDistanceFromLatLonInNm(arrapt_latlon[0],arrapt_latlon[1],pt40arr[0],pt40arr[1])<40)
			{i40arr=i40arr-1;
			pt40arr=d.geometry.coordinates[i40arr];}

		pt100arr=d.geometry.coordinates[d.geometry.coordinates.length-2]; i100arr=d.geometry.coordinates.length-2;
		while (getDistanceFromLatLonInNm(arrapt_latlon[0],arrapt_latlon[1],pt100arr[0],pt100arr[1])<100)
			{i100arr=i100arr-1;
			pt100arr=d.geometry.coordinates[i100arr];}
		// Compute the achieved distance (last point-first point)
		achieved_dist40to40=getDistanceFromLatLonInNm(pt40dep[0],pt40dep[1],pt40arr[0],pt40arr[1]);
		achieved_dist40to100=getDistanceFromLatLonInNm(pt40dep[0],pt40dep[1],pt100arr[0],pt100arr[1]);
		achieved_dist100to100=getDistanceFromLatLonInNm(pt100dep[0],pt100dep[1],pt100arr[0],pt100arr[1]);
		// Compute the flight time for each
		travel_time_40to40=(d.geometry.times[i40arr]-d.geometry.times[i40dep])/60000;// in minutes
		travel_time_40to100=(d.geometry.times[i100arr]-d.geometry.times[i40dep])/60000;
		travel_time_100to100=(d.geometry.times[i100arr]-d.geometry.times[i100dep])/60000;
		if (travel_time_100to100<0){
			travel_time_100to100=(d.geometry.times[i100arr+1]-d.geometry.times[i100dep-1])/60000; //a few short flights have problems with indexes otherwise
		}
		//Compute the total flight distance from 40 to 40 - sum the distance between each consecutive point
		total_dist40to40=0;
		total_dist40to100=0;
		total_dist100to100=0;
		//for (var ipt=i40dep; ipt < i40arr; ipt++) {
		for (var ipt=i40dep-1; ipt < i40arr+1; ipt++) {
			total_dist40to40=total_dist40to40+getDistanceFromLatLonInNm(d.geometry.coordinates[ipt][0],d.geometry.coordinates[ipt][1],
				d.geometry.coordinates[ipt+1][0],d.geometry.coordinates[ipt+1][1]);
		}
		//add the extra that might me missing because no i40dep point is exactly 40 nm away from the dep apt
		total_dist40to40=total_dist40to40+getDistanceFromLatLonInNm(depapt_latlon[0],depapt_latlon[1],d.geometry.coordinates[i40dep][0],d.geometry.coordinates[i40dep][1])+getDistanceFromLatLonInNm(arrapt_latlon[0],arrapt_latlon[1],d.geometry.coordinates[i40arr][0],d.geometry.coordinates[i40arr][1])-80;

		for (var ipt=i40dep; ipt < i100arr; ipt++) {
			total_dist40to100=total_dist40to100+getDistanceFromLatLonInNm(d.geometry.coordinates[ipt][0],d.geometry.coordinates[ipt][1],
				d.geometry.coordinates[ipt+1][0],d.geometry.coordinates[ipt+1][1]);
		}
		total_dist40to100=total_dist40to100+getDistanceFromLatLonInNm(depapt_latlon[0],depapt_latlon[1],d.geometry.coordinates[i40dep][0],d.geometry.coordinates[i40dep][1])+getDistanceFromLatLonInNm(arrapt_latlon[0],arrapt_latlon[1],d.geometry.coordinates[i100arr][0],d.geometry.coordinates[i100arr][1])-140;
		
		for (var ipt=i100dep; ipt < i100arr; ipt++) {
			total_dist100to100=total_dist100to100+getDistanceFromLatLonInNm(d.geometry.coordinates[ipt][0],d.geometry.coordinates[ipt][1],
				d.geometry.coordinates[ipt+1][0],d.geometry.coordinates[ipt+1][1]);
		}	
		total_dist100to100=total_dist100to100+getDistanceFromLatLonInNm(depapt_latlon[0],depapt_latlon[1],d.geometry.coordinates[i100dep][0],d.geometry.coordinates[i100dep][1])+getDistanceFromLatLonInNm(arrapt_latlon[0],arrapt_latlon[1],d.geometry.coordinates[i100arr][0],d.geometry.coordinates[i100arr][1])-200;

		//check for unusually small values - ie length of trajectory 		
		if (total_dist40to40<apt2apt_dist-80){ //underestimation - to be verified - filtered weird trajectories
			achieved_dist40to40=-1;
			achieved_dist40to100=-1;
			achieved_dist100to100=-1;
			total_dist40to40=-1;
			total_dist40to100=-1;
			total_dist100to100=-1;
			travel_time_40to40=-1;
			travel_time_40to100=-1;
			travel_time_100to100=-1;
		}
		// //check for unusually large values
		// if (total_dist40to40>apt2apt_dist*1.5){
		// 	achieved_dist40to40=-1;
		// 	achieved_dist40to100=-1;
		// 	achieved_dist100to100=-1;
		// 	total_dist40to40=-1;
		// 	total_dist40to100=-1;
		// 	total_dist100to100=-1;
		// 	travel_time_40to40=-1;
		// 	travel_time_40to100=-1;
		// 	travel_time_100to100=-1;
		// 	console.log(d.geometry.coordinates,apt2apt_dist,total_dist40to40)
			
		// }

		//return values
		metric={achieved_dist40to40:achieved_dist40to40,
			achieved_dist40to100:achieved_dist40to100,
			achieved_dist100to100:achieved_dist100to100,
			travel_time_40to40:travel_time_40to40,
			travel_time_40to100:travel_time_40to100,
			travel_time_100to100:travel_time_100to100,
			total_dist40to40:total_dist40to40,
			total_dist40to100:total_dist40to100,
			total_dist100to100:total_dist100to100};

	}
	else {
		metric={achieved_dist40to40:-1,
			achieved_dist40to100:-1,
			achieved_dist100to100:-1,
			travel_time_40to40:-1,
			travel_time_40to100:-1,
			travel_time_100to100:-1,
			total_dist40to40:-1,
			total_dist40to100:-1,
			total_dist100to100:-1};
	}
	// d.metrics = metric;
	//console.log(metric);
	return metric;
	
}

        
function set_query_status(drawing){
	if (drawing){
	    spinner.spin(target);
	} else {
	    spinner.stop();
	}
}

    
function displayFlightInfo(d) {
	// console.log(d);
	popup_create(d);reset_popup_timer();
}

// Use Leaflet to implement a D3 geometric transformation.
function projectPoint(x, y) {
	var point = map.latLngToLayerPoint(new L.LatLng(y, x));
	this.stream.point(point.x, point.y);
}


function refresh_info_panel() {
	// get metrics info
	bounds = map.getBounds();
	var sw = bounds._southWest;
	var ne = bounds._northEast;
	var se = new L.LatLng(sw.lat,ne.lng);
	map_height = Math.ceil(ne.distanceTo(se)/1000);
	map_width = Math.ceil(sw.distanceTo(se)/1000);
	// update UI
	info_zoom.text("Zoom:\t".concat(map.getZoom()));
	info_width.text("Width:\t".concat(map_width," km"));
	info_height.text("Height:\t".concat(map_height," km"));
}

// "ARR_APRT": "LGA",
// "GEO_CENTER": "",
// "ARL_COD": "AAL",
// "FPA": "",
// "CENTER": "R",
// "FLIGHT_INDEX": "102325",
// "ORIG_ACT_DATE": "05-MAR-14",
// "FLI_NUM": "2368",
// "BEACON_CODE": "1372",
// "ALTITUDE_TYPE": "",
// "ARR_FIX_TIME": "05-MAR-14",
// "ORIG_INDEX": "102325",
// "POSIT_TIME": "05-MAR-14",
// "POINT_STATUS": "-1",
// "ORIG_TIME": "05-MAR-14",
// "CID": "279",
// "FID": "20140305148298",
// "DEP_FIX_TIME": "05-MAR-14",
// "ARR_ESTIMATE": "05-MAR-14",
// "DEPT_APRT": "MIA",
// "ACT_DATE": "05-MAR-14"

function popup_create(d){
	var titleHtml = d.ori + " -> " + d.dest + "</br>";
	titleHtml += d.airline + d.flight_num + "</br>";

	var contentHtml = "";
	contentHtml += "Tail: " + d.tail_num +"</br></br>";
	contentHtml += "Scheduled: " + d.sched_dep +"-"+d.sched_arr +"</br>";
	contentHtml += "Actual: " + d.actual_dep +"-"+d.actual_arr +"</br>";

	invoke_popup(titleHtml,contentHtml);
}

function popup_create2(d){
	var titleHtml = d.DEPT_APRT + " -> " + d.ARR_APRT + "</br>";
	titleHtml += d.ARL_COD + d.FLI_NUM + "</br>";

	var contentHtml = "";
	contentHtml += datetimeformat.parse(d.ORIG_DATE+"T"+d.ORIG_TIME)+"</br>";
	contentHtml += "Tail: " + d.BEACON_CODE +"</br></br>";
	contentHtml += "Scheduled: " + 'xxxx' +"-"+'xxxx' +"</br>";
	contentHtml += "Actual: " + 'xxxx' +"-"+'xxxx' +"</br>";

	invoke_popup(titleHtml,contentHtml);
}

function fade_out_popup() {
	d3.select('#pop-up')
	  .transition()
	  .style('opacity', 0)
	  .duration(250);

	setTimeout(function () {
		d3.select('#pop-up')
		  .style('display', 'none');
	}, 250);
}

function fade_in_popup() {
	d3.select('#pop-up')
	  .transition()
	  .style('opacity', 100)
	  .style('display', 'block')
	  .duration(3000);
}



function invoke_popup(titleHtml, contentHtml, numLines) {
	e = d3.event;
	var p = d3.select('#pop-up');

	var pl = e.pageX + 50;
	var pt = e.pageY - 25;
	
	p.style('left', '20px')
	 .style('top', '60%');

	d3.select('#pop-up-title').html(titleHtml);
	d3.select('#pop-up-content').html(contentHtml);
	fade_in_popup();

	reset_popup_timer();
}

function reset_popup_timer() {
	if (popupTimer) {
		clearTimeout(popupTimer);
	}

	popupTimer = setTimeout(fade_out_popup, 5000);
}

function airline_sort(a,b){
	return d3.descending(a.num, b.num);
}

function update_airlines(mflights){
	airlines_list = {};
	selected_ARL = [];
	airlines =[];
	d3.select("#airlines-list").selectAll("ul").remove();
	list = d3.select("#airlines-list").append("ul");
	list.selectAll("input").remove();

	for (i = 0; i < mflights.features.length; i++) { 
			if (airlines_list.hasOwnProperty(mflights.features[i].properties.ARL_COD)) {
				airlines_list[mflights.features[i].properties.ARL_COD] = airlines_list[mflights.features[i].properties.ARL_COD]+1;
			}else {
				airlines_list[mflights.features[i].properties.ARL_COD] = 1;
			}
		}

	for (var key in airlines_list) {
	    airlines.push({"name":key,"num":airlines_list[key]});
	    selected_ARL.push(key);
	}	
	items = list.selectAll("input")
		.data(airlines.sort(airline_sort))
		.enter()
		.append("label")
		.text(function(d){return d.name+": "+d.num})
		.style("margin-right","10px")
		.append("input")
		.attr("type", "checkbox")
		.attr('checked','true')
		.attr("id",function(d){return d.name})
		.on("click", function(d){
			// console.log(d.name)
			if (selected_ARL.indexOf(d.name)>-1){
				g.selectAll("path")
					.filter(function(i){return i.properties.ARL_COD===d.name})
					.filter(function(i){return selected_OD.indexOf(i.properties.DEPT_APRT+'-'+i.properties.ARR_APRT)>-1})
					.each(function(d){d.displayed="False"})
					.style("display", "none");
				selected_ARL.splice(selected_ARL.indexOf(d.name),1);
			} else {
				g.selectAll("path")
					.filter(function(i){return i.properties.ARL_COD===d.name})
					.filter(function(i){return selected_OD.indexOf(i.properties.DEPT_APRT+'-'+i.properties.ARR_APRT)>-1})
					.each(function(d){d.displayed="True"})
					.style("display", null);
				selected_ARL.push(d.name)
			}
			displayed_flights = searched_flights.features//g.selectAll("path")
				.filter(function(d){return d.displayed=="True"});
			draw_metrics(displayed_flights);
			// console.log(displayed_flights.length);
			d3.select("#info_flights_num").text("#Flights: "+displayed_flights.length);
			d3.select("#info_flights_ARL").text("#Airlines: "+selected_ARL.length);
		
			update_opacity();
		});
}

function update_ori_dest(mflights){
	ori_dest_list = {};
	selected_OD = [];
	ori_dest = [];
	d3.select("#ori-dest-list").selectAll("ul").remove();
	list = d3.select("#ori-dest-list").append("ul");
	list.selectAll("input").remove();

	for (i = 0; i < mflights.features.length; i++) { 
		ori_dest_i = mflights.features[i].properties.DEPT_APRT+'-'+mflights.features[i].properties.ARR_APRT;
			if (ori_dest_list.hasOwnProperty(ori_dest_i)) {
				ori_dest_list[ori_dest_i] = ori_dest_list[ori_dest_i]+1;
			}else {
				ori_dest_list[ori_dest_i] = 1;
			}
		}

	for (var key in ori_dest_list) {
	    ori_dest.push({"name":key,"num":ori_dest_list[key]});
	    selected_OD.push(key);
	}	
	items = list.selectAll("input")
		.data(ori_dest.sort(airline_sort))
		.enter()
		.append("label")
		.text(function(d){return d.name+": "+d.num})
		.style("margin-right","10px")
		.append("input")
		.attr("type", "checkbox")
		.attr('checked','true')
		.attr("id",function(d){return d.name})
		.on("click", function(d){
			// console.log(d.name)
			if (selected_OD.indexOf(d.name)>-1){
				g.selectAll("path")
					.filter(function(i){return (i.properties.DEPT_APRT+'-'+i.properties.ARR_APRT)===d.name})
					.filter(function(i){return selected_ARL.indexOf(i.properties.ARL_COD)>-1})
					.each(function(d){d.displayed="False"})
					.style("display", "none");
				selected_OD.splice(selected_OD.indexOf(d.name),1);
			} else {
				g.selectAll("path")
					.filter(function(i){return (i.properties.DEPT_APRT+'-'+i.properties.ARR_APRT)===d.name})
					.filter(function(i){return selected_ARL.indexOf(i.properties.ARL_COD)>-1})
					.each(function(d){d.displayed="True"})
					.style("display", null);
				selected_OD.push(d.name)
			}
			displayed_flights = searched_flights.features//g.selectAll("path")
				.filter(function(d){return d.displayed=="True"});
			draw_metrics(displayed_flights);
			// console.log(displayed_flights.length);
			d3.select("#info_flights_num").text("#Flights: "+displayed_flights.length);
			d3.select("#info_flights_ARL").text("#Airlines: "+selected_ARL.length);
		
			update_opacity();
		});
}

function checkAll_OD(){
	selected_OD = [];
    d3.select("#ori-dest-list").selectAll('input').property('checked',true);
    g.selectAll("path")
    	.filter(function(i){return selected_ARL.indexOf(i.properties.ARL_COD)>-1})
		.each(function(d){d.displayed="True"})
		.style("display", null);
	d3.select("#ori-dest-list").selectAll('input')
		.property('checked',true);
	for (var key in ori_dest_list) {
	    selected_OD.push(key);
	}	

	displayed_flights = searched_flights.features//g.selectAll("path")
		.filter(function(d){return d.displayed=="True"});
	draw_metrics(displayed_flights);
	d3.select("#info_flights_num").text("#Flights: "+displayed_flights.length);

	update_opacity();
}
function uncheckAll_OD(){
    d3.select("#ori-dest-list").selectAll('input').property('checked',false);
    g.selectAll("path")
    	.each(function(d){d.displayed="False"})
		.style("display", "none");
	d3.select("#ori-dest-list").selectAll('input')
		.property('checked',false);
    selected_OD = [];

	displayed_flights = searched_flights.features//g.selectAll("path")
		.filter(function(d){return d.displayed=="True"});
	draw_metrics(displayed_flights);
	d3.select("#info_flights_num").text("#Flights: "+displayed_flights.length);
}

function checkAll_ARL(){
	selected_ARL = [];
    d3.select("#airlines-list-list").selectAll('label').selectAll('input')
    	.property('checked',true);
    g.selectAll("path")
    	.filter(function(i){return selected_OD.indexOf(i.properties.DEPT_APRT+'-'+i.properties.ARR_APRT)>-1})
		.each(function(d){d.displayed="True"})
		.style("display", null);
	d3.select("#airlines-list").selectAll('input')
		.property('checked',true);
	for (var key in airlines_list) {
	    selected_ARL.push(key);
	}
	
	displayed_flights = searched_flights.features//g.selectAll("path")
		.filter(function(d){return d.displayed=="True"});
	d3.select("#info_flights_num").text("#Flights: "+displayed_flights.length);
	d3.select("#info_flights_ARL").text("#Airlines: "+selected_ARL.length);

	update_opacity();
	draw_metrics(displayed_flights);
}
function uncheckAll_ARL(){
    d3.select("#airlines-list").selectAll('label').selectAll('input').property('checked',false);
    g.selectAll("path")
	    .each(function(d){d.displayed="False"})
		.style("display", "none");
	d3.select("#airlines-list").selectAll('input')
		.property('checked',false);
    selected_ARL =[];
	
	displayed_flights = searched_flights.features//g.selectAll("path")
		.filter(function(d){return d.displayed=="True"});
	draw_metrics(displayed_flights);
	d3.select("#info_flights_num").text("#Flights: "+displayed_flights.length);
	d3.select("#info_flights_ARL").text("#Airlines: "+selected_ARL.length);
}
 function alert_popup(textMessage){
 	$("#dialog-message").dialog({
    modal: true,
    draggable: false,
    resizable: false,
    position: ['center', 'top'],
    show: 'blind',
    hide: 'blind',
    width: 400,
    dialogClass: 'ui-dialog-osx',
    buttons: {
        "I've read and understand this": function() {
            $(this).dialog("close");
        }
    }
});
 }