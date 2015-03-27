// google.maps.event.addDomListener(window, 'load');
function generateHeader(){
	var temp = '';
	temp = '{"query":{"filtered":{"query":{"match_all":{}},"filter":{"nested":{"path":"AIR","query":{"filtered":{"query":{"match_all":{}},"filter":{"and": [';
	return temp;
}
function generateARL_COD(){
	var temp = '';
	if ($('#AirlineCode').val() !==''){
		temp = '{"term": {"AIR.ARL_COD": "' + $('#AirlineCode').val() + '"}},';
	}
	return temp;
}
function generateDEP_ARP(){
	var temp='';
	if ($('#DEPT_APRT').val() !==''){
		temp = '{"term": {"AIR.DEP_APRT": "' + $('#DEPT_APRT').val() + '"}},';
	}	
	return temp;
}
function generateARR_APRT(){
	var temp='';
	if ($('#ARR_APRT').val() !==''){
		temp = '{"term": {"AIR.ARR_APRT": "' + $('#ARR_APRT').val() + '"}},';
	}	
	return temp;
}
function generateFLI_NUM(){
	var temp='';
	if ($('#FLI_NUM').val() !==''){
		temp = '{"term": {"AIR.FLI_NUM": "' + $('#FLI_NUM').val() + '"}},';
	}
	return temp;
}
function generateArrDate(){
	var temp='';
	if ($('#ArrDate_from').val() !==''){
		temp = '{"range": {"AIR.ARR_EST_DATE": {"from":"' + $('#ArrDate_from').val() + '","to":"'+ $('#ArrDate_to').val() +'"}}},';
	}
	return temp;
}
function generateDepDate(){
	var temp='';
	if ($('#DepDate_from').val() !==''){
		temp = '{"range": {"AIR.ORIG_DATE": {"from":"' + $('#DepDate_from').val() + '","to":"'+ $('#DepDate_to').val() +'"}}},';
	}
	return temp;
}
function generateArrTime(){
	var temp='';
	if ($('#ArrTime_from').val() !==''){
		temp = '{"range": {"AIR.ARR_EST_TIME": {"from":"' + $('#ArrTime_from').val() + '","to":"'+ $('#ArrTime_to').val() +'"}}},';
	}
	return temp;
}
function generateDepTime(){
	var temp='';
	if ($('#DepTime_from').val() !==''){
		temp = '{"range": {"AIR.ORIG_TIME": {"from":"' + $('#DepTime_from').val() + '","to":"'+ $('#DepTime_to').val() +'"}}},';
	}
	return temp;
}
var from_=0;
function next(){
	dispsize_ = $('#num_plot').val();
	if (dispsize_ == ''){
		dispsize_ = 5000;
	}
	from_ = from_ + parseInt(dispsize_);
	search()
}

function previous(){
	dispsize_ = $('#num_plot').val();
	if (dispsize_ == ''){
		dispsize_ = 5000;
	}
	from_= from_ - dispsize_;
	if (from_ <0) {
		from_ = 0;
	}
	search()
}

function nm2km(){	
	if ($('#radius').val() !==''){
		var temp = $('#radius').val()*1.852;
	}
	return temp;
}
function get_coord(){
	var temp='';
	if ($('#lat').val()!=='' && $('#long').val()!==''){
	//alert('latlongselected')
		temp = '['+$('#long').val()+','+$('#lat').val()+']';
	}
	else if ($('#APRT').val()!==''){
		//alert('aprt selected')
		if 	($('#APRT').val() == 'LGA'){
			temp = '[-73.8726,40.7772]';
		}
		else if ($('#APRT').val() == 'JFK'){
			temp = '[-73.7789,40.6397]';
		}
		else if ($('#APRT').val() == 'MIA'){
			temp = '[-80.2906,25.7933]';
		}
		else if ($('#APRT').val() == 'SFO'){
			temp = '[-122.3754281,37.6188172]';
		}
		else if ($('#APRT').val() == 'DFW'){
			temp = '[-97.0381,32.8969]';
		}
	}
	return temp;
}
function generateRadius(){
	var temp='';
	temp = '{"query":{"filtered":{"query":{"match_all":{}},"filter":{"and":[{"geo_shape":{"LOCATION":{"shape":{"type":"circle","coordinates":'+ get_coord()+',"radius":"'+nm2km()+'km"}}}}]}}}}'
	//alert(temp)
	return temp;
}
function generateQuery(){
	temp='';
	if ($('#DEPT_APRT').val()=='' && $('#ARR_APRT').val()==''&& $('#AirlineCode').val()==''&& $('#FLI_NUM').val()==''){
		alert('Please select at least one category');
	}
	else if ($('#radius').val()!==''&& ($('#DEPT_APRT').val()!== '' && $('#ARR_APRT').val()!==''&& $('#AirlineCode').val()!==''&& $('#FLI_NUM').val()!=='')){
		//alert('radius')
		//alert($('#DEPT_APRT').val())
		temp = generateRadius();
	}
	else if($('#radius').val()=='' && ($('#DEPT_APRT').val()!== '' || $('#ARR_APRT').val()!==''|| $('#AirlineCode').val()!==''|| $('#FLI_NUM').val()!=='')){
		//alert('not radius')
		temp = removeLastComma(generateHeader() + generateARL_COD() + generateDEP_ARP() + generateARR_APRT() + generateFLI_NUM() + generateArrDate()+ generateDepDate() + generateDepTime()+ generateArrTime()+']}}}}}}}}');
	}
	else if($('#radius').val()!=='' && ($('#DEPT_APRT').val()!== '' || $('#ARR_APRT').val()!==''|| $('#AirlineCode').val()!==''|| $('#FLI_NUM').val()!=='')){
		//alert('city and radius')
		temp = generateRadius().substring(0, + generateRadius().length-5) + ',' + removeLastComma(generateHeader().substring(56, + generateHeader().length) + generateARL_COD() + generateDEP_ARP() + generateARR_APRT() + generateFLI_NUM() + generateArrDate()+ generateDepDate() + generateDepTime()+ generateArrTime()+']}}}}}]}}}}'); 
	}
	//document.getElementById("demo_adress").innerHTML=temp;
	//alert(temp)
	//$("#query").html(library.json.prettyPrint(JSON.parse(temp)));
	return temp;
}
function removeLastComma(s) {
   var n = s.lastIndexOf(',');
   s = s.substring(0, n) + '' + s.substring(n + 1);
   return s
}
function initialize() {
	var mapOptions = {
		zoom: 3,
		center: new google.maps.LatLng(0, -180),
		mapTypeId: google.maps.MapTypeId.TERRAIN
	};

	// var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	/*var flightPlanCoordinates = [
		new google.maps.LatLng(37.772323, -122.214897),
		new google.maps.LatLng(21.291982, -157.821856),
		new google.maps.LatLng(-18.142599, 178.431),
		new google.maps.LatLng(-27.46758, 153.027892)
	];*/
	//map.data.loadGeoJson(obj2.hits.hits[0]._source.LOCATION);
	//map.data.loadGeoJson('http://localhost/Aude/wookie.json');
	// var flightPath = new google.maps.Polyline({
	// //path: flightPlanCoordinates,
	// geodesic: true,
	// strokeColor: '#FF0000',
	// strokeOpacity: 1.0,
	// strokeWeight: 2
	// });

	// flightPath.setMap(map);
}
// google.maps.event.addDomListener(window, 'load', initialize);
/*function hide(){
	$('#query').hide();
	$('#results').hide();
}	
function show(){
	$('#query').show();
	$('#results').show();
}	
$(document).ready(function () {
	$('#query').hide();
	$('#results').hide();
});*/
//---------------------------------------SEARCH----------------------------------------
function DispSize() {
		var dispsize_='';
		var query1='';
		dispsize_ = $('#num_plot').val()	
		if (dispsize_ == ''){
			dispsize_=5000;
			query1 = "from="+from_+"&size="+dispsize_;
					}
		else if (isNaN(dispsize_) == 0){
			query1= "from="+from_+"&size="+dispsize_;
		}
		else if (isNaN(dispsize_) == 1){
			alert("Not a Number")	
		}
		//alert(query)
	return query1;	
}
var responseText = '';
// var obj = {};

function search() {
	var url = "http://localhost:9200/" + 'faa_nextor_flight_traj_plan/_search?' + DispSize();
	//var url2 = "http://localhost:9200/" + 'faa_nextor_flightplan/_search?' + DispSize();
	$("#demo_adress").html(DispSize());
	var client = new XMLHttpRequest();
	client.open("POST", url, false);
	client.setRequestHeader("Content-Type", "text/plain");
	try {
		client.send(generateQuery());
	} catch(err) {
	    alert('The query was not sent. There is probably a connection problem with the server!\nRemember to forward port 9200 of cicero on your 9200');
	    // spinner.stop()
	}
	if (client.status != 200){
		alert('There was an error with your request!\n'+client.statusText);
		// spinner.stop()
    } else {
		var obj = JSON.parse(client.responseText);
		// responseText = client.responseText;

			extract_raw_data(obj);
			// d3.json(client.responseText, function(error,data){
			// 	if (!error && typeof data !== 'undefined'){

			// 	// me
			// 	searched_flights = {};
			// 	searched_flights.features = data.hits.hits;
			// 	searched_flights.type = "FeatureCollection";
			// 	delete searched_flights._type;
			// 	delete searched_flights._score;
			// 	for (i = 0; i < searched_flights.features.length; i++) { 
			// 	    searched_flights.features[i].type = "Feature";
			// 	    searched_flights.features[i].geometry = searched_flights.features[i]._source.LOCATION[0];
			// 	    // console.log(searched_flights.features[i]._source)
			// 	    searched_flights.features[i].altitude = searched_flights.features[i]._source.POSITION[0].ALTITUDE;
			// 	    searched_flights.features[i].groundspeed = searched_flights.features[i]._source.POSITION[0].GROUNDSPEED;
			// 	    delete searched_flights.features[i]._source.LOCATION;
			// 	    searched_flights.features[i].geometry.type = "LineString"
			// 	    searched_flights.features[i].properties = searched_flights.features[i]._source.AIR[0];
			// 	}
			// 	console.log("start drawing");
			// 	flights = searched_flights;
			// 	draw_flights(searched_flights);
			// 	console.log("done drawing");
			// 	}
			// });
	}
	///////////////////////////////////////////////////////////////////
	// var client2 = new XMLHttpRequest();
	// client2.open("POST", url2, false);
	// client2.setRequestHeader("Content-Type", "text/plain");
	// try {
	// 	client2.send(generateQuery2());
	// } catch(err) {
	//     alert('The query for plans was not sent. There is probably a connection problem with the server!\nRemember to forward port 9200 of cicero on your 9200');
	//     // spinner.stop()
	// }
	// if (client2.status != 200){
	// 	alert('There was an error with your request! (plans)\n'+client2.statusText);
	// 	// spinner.stop()
 //    } else {
	// 	var obj2 = JSON.parse(client2.responseText);
	// 	// responseText = client.responseText;

	// 	if (obj2.hits.hits.length>0){
	// 		searched_flightplans_LA = {};
	// 		searched_flightplans_LA.features = obj2.hits.hits;
	// 		// console.log(searched_flightplans.features);
	// 		searched_flightplans_LA.type = "FeatureCollection";
	// 		delete searched_flightplans_LA._type;
	// 		delete searched_flightplans_LA._score;
			
	// 		searched_flightplans_LF = {};
	// 		searched_flightplans_LF.features = obj2.hits.hits;
	// 		searched_flightplans_LF.type = "FeatureCollection";
	// 		delete searched_flightplans_LF._type;
	// 		delete searched_flightplans_LF._score;
			
	// 		searched_flightplans_PD = {};
	// 		searched_flightplans_PD.features = obj2.hits.hits;
	// 		searched_flightplans_PD.type = "FeatureCollection";
	// 		delete searched_flightplans_PD._type;
	// 		delete searched_flightplans_PD._score;
	// 		////
			
			
			
	// 		for (i = 0; i < searched_flightplans_LA.features.length; i++) { 
	// 			searched_flightplans_LA.features[i].datatype = "plan";
	// 		    searched_flightplans_LA.features[i].type = "Feature";
	// 			//LF = searched_flightplans.features[1]._source.LF[0].FPWAYPT_coord
	// 			//PD = searched_flightplans.features[1]._source.PD[0].FPWAYPT_coord
	// 			//LA = searched_flightplans.features[1]._source.LA[0].FPWAYPT_coord
	// 			searched_flightplans_LA.features[i].geometry={};
	// 			searched_flightplans_LA.features[i].geometry = searched_flightplans_LA.features[i]._source.LA[0].FPWAYPT_coord[0]
	// 			//searched_flightplans.features[i].geometry.coordinates={};
	// 		    //searched_flightplans.features[i].geometry.coordinates = searched_flightplans.features[i]._source.LF[0].FPWAYPT_coord[0]
	// 			searched_flightplans_LA.features[i].properties={};
	// 			searched_flightplans_LA.features[i].properties = searched_flightplans_LA.features[i]._source.AIR[0]
	// 		    // searched_flights.features[i].altitude = searched_flights.features[i]._source.POSITION[0].ALTITUDE;
	// 		    // searched_flights.features[i].groundspeed = searched_flights.features[i]._source.POSITION[0].GROUNDSPEED;
	// 		//    delete searched_flightplans.features[i]._source.LOCATION;
	// 		//    delete searched_flightplans.features[i]._source.POSITION;
	// 		    searched_flightplans_LA.features[i].geometry.type = "LineString";
	// 		    //searched_flightplans.features[i].properties = searched_flightplans.features[i]._source.AIR[0];
	// 		    //searched_flightplans.features[i].metrics = compute_metrics(searched_flightplans.features[i])
				
	// 			searched_flightplans_LF.features[i].datatype = "plan";
	// 		    searched_flightplans_LF.features[i].type = "Feature";
	// 			searched_flightplans_LF.features[i].geometry={};
	// 			searched_flightplans_LF.features[i].geometry = searched_flightplans_LF.features[i]._source.LF[0].FPWAYPT_coord[0]
	// 			searched_flightplans_LF.features[i].properties={};
	// 			searched_flightplans_LF.features[i].properties = searched_flightplans_LF.features[i]._source.AIR[0]
	// 		    searched_flightplans_LF.features[i].geometry.type = "LineString";
				
	// 			searched_flightplans_PD.features[i].datatype = "plan";
	// 		    searched_flightplans_PD.features[i].type = "Feature";
	// 			searched_flightplans_PD.features[i].geometry={};
	// 			searched_flightplans_PD.features[i].geometry = searched_flightplans_PD.features[i]._source.PD[0].FPWAYPT_coord[0]
	// 			searched_flightplans_PD.features[i].properties={};
	// 			searched_flightplans_PD.features[i].properties = searched_flightplans_PD.features[i]._source.AIR[0]
	// 		    searched_flightplans_PD.features[i].geometry.type = "LineString";
	// 		}
	// 		console.log("start drawing plans");
	// 		draw_flights(searched_flightplans_LA,"LA");
	// 		draw_flights(searched_flightplans_LF,"LF");
	// 		draw_flights(searched_flightplans_PD,"PD");
	// 		//draw_metrics(searched_flightplans.features);
	// 		console.log("done drawing plans");
	// 	}else {
	// 		alert("No plans for the corresponding query");
	// 	}
	// }
}
$(function() {
    $( "#ArrDate_from" ).datepicker({
		minDate: new Date(2014, 0 , 1),
		maxDate: new Date(2014, 6 , 1),
		changeMonth: true,
		changeYear: true,
		showOtherMonths: true,
		selectOtherMonths: true,
		showButtonPanel: true,
		dateFormat: 'dd-M-y',
		showWeek: true,
		firstDay:1
    });
});
$(function() {
    $( "#ArrDate_to" ).datepicker({
		minDate: new Date(2014, 0 , 1),
		maxDate: new Date(2014, 6 , 1),
		changeMonth: true,
		changeYear: true,
		showOtherMonths: true,
		selectOtherMonths: true,
		showButtonPanel: true,
		dateFormat: 'dd-M-y',
		showWeek: true,
		firstDay:1
    });
});
$(function() {
    $( "#DepDate_from" ).datepicker({
		minDate: new Date(2014, 0 , 1),
		maxDate: new Date(2014, 6 , 1),
		changeMonth: true,
		changeYear: true,
		showOtherMonths: true,
		selectOtherMonths: true,
		showButtonPanel: true,
		dateFormat: 'dd-M-y',
		showWeek: true,
		firstDay:1
    });
});
$(function() {
    $( "#DepDate_to" ).datepicker({
		minDate: new Date(2014, 0 , 1),
		maxDate: new Date(2014, 6 , 1),
		changeMonth: true,
		changeYear: true,
		showOtherMonths: true,
		selectOtherMonths: true,
		showButtonPanel: true,
		dateFormat: 'dd-M-y',
		showWeek: true,
		firstDay:1
    });
});
if (!library) var library = {};
library.json = {
   replacer: function(match, pIndent, pKey, pVal, pEnd) {
	  var key = '<span class=json-key>';
	  var val = '<span class=json-value>';
	  var str = '<span class=json-string>';
	  var r = pIndent || '';
	  if (pKey)
		 r = r + key + pKey.replace(/[": ]/g, '') + '</span>: ';
	  if (pVal)
		 r = r + (pVal[0] == '"' ? str : val) + pVal + '</span>';
	  return r + (pEnd || '');
	  },
   prettyPrint: function(obj) {
	  var jsonLine = /^( *)("[\w]+": )?("[^"]*"|[\w.+-]*)?([,[{])?$/mg;
	  return JSON.stringify(obj, null, 3)
		 .replace(/&/g, '&amp;').replace(/\\"/g, '&quot;')
		 .replace(/</g, '&lt;').replace(/>/g, '&gt;')
		 .replace(jsonLine, library.json.replacer);
	  }
   };
