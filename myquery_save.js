google.maps.event.addDomListener(window, 'load');
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
		temp = '{"term": {"AIR.DEPT_APRT": "' + $('#DEPT_APRT').val() + '"}},';
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
		temp = '{"range": {"AIR.ARR_ESTIMATE": {"from":"' + $('#ArrDate_from').val() + '","to":"'+ $('#ArrDate_to').val() +'"}}},';
	}
	return temp;
}

function generateQuery(){
	temp='';
	if ($('#DEPT_APRT')=='' && $('#ARR_APRT')==''&& $('#AirlineCode')==''&& $('#FLI_NUM')==''){
		alert('Please select at least one category');
	}
	else if($('#DEPT_APRT')!== '' || $('#ARR_APRT')!==''|| $('#AirlineCode')!==''|| $('#FLI_NUM')!==''){
		temp = removeLastComma(generateHeader() + generateARL_COD() + generateDEP_ARP() + generateARR_APRT() + generateFLI_NUM() + generateArrDate()+']}}}}}}}}');
	}
	//document.getElementById("demo_adress").innerHTML=temp;
	$("#query").html(library.json.prettyPrint(JSON.parse(temp)));
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

	var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	/*var flightPlanCoordinates = [
		new google.maps.LatLng(37.772323, -122.214897),
		new google.maps.LatLng(21.291982, -157.821856),
		new google.maps.LatLng(-18.142599, 178.431),
		new google.maps.LatLng(-27.46758, 153.027892)
	];*/
	//map.data.loadGeoJson(obj2.hits.hits[0]._source.LOCATION);
	map.data.loadGeoJson('http://localhost/Aude/wookie.json');
	var flightPath = new google.maps.Polyline({
	//path: flightPlanCoordinates,
	geodesic: true,
	strokeColor: '#FF0000',
	strokeOpacity: 1.0,
	strokeWeight: 2
	});

	flightPath.setMap(map);
}
google.maps.event.addDomListener(window, 'load', initialize);
function hide(){
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
});
//---------------------------------------SEARCH----------------------------------------
function search() {
	//var url = "http://localhost:9200/" + 'ironman/_search'
	var url = "http://128.61.186.135:9200/" + 'faa_nextor/_search'
	
	var client = new XMLHttpRequest();
	client.open("POST", url, false);
	client.setRequestHeader("Content-Type", "text/plain");
	client.send(generateQuery() + '&pretty');
	var obj = JSON.parse(client.responseText);
	console.log(client.responseText);
	$("#results").html(library.json.prettyPrint(obj));
	var temp = client.responseText;
	obj2 = JSON.parse(temp);

	// me
	searched_flights = {};
	searched_flights.features = obj.hits.hits;
	searched_flights.type = "FeatureCollection";
	delete searched_flights._type;
	delete searched_flights._score;
	for (i = 0; i < searched_flights.features.length; i++) { 
	    searched_flights.features[i].type = "feature";
	    searched_flights.features[i].geometry = searched_flights.features[i]._source.LOCATION[0];
	    delete searched_flights.features[i]._source.LOCATION;
	    searched_flights.features[i].geometry.type = "LineString"
	    searched_flights.features[i].properties = searched_flights.features[i]._source.AIR;
	}
	draw_flights(searched_flights);
	//document.getElementById("demo_adress").innerHTML = JSON.stringify(obj2.hits.hits[0]._source.LOCATION)
	// if(obj2.hits.hits[0]._source.LOCATION !== undefined){
	// 	//alert('Wookie');
	// 	google.maps.event.addDomListener(window, 'load', initialize);
	// }
}
$(function(){
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
    $( "#DepDate" ).datepicker({
		minDate: new Date(2014, 0 , 1),
		maxDate: new Date(2014, 6 , 1),
		changeMonth: true,
		changeYear: true,
		showOtherMonths: true,
		selectOtherMonths: true,
		showButtonPanel: true,
		dateFormat: 'yy-mm-dd',
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