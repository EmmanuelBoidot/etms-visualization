var dept_aprt_in_db = [];
var arr_aprt_in_db = [];
var airlines_in_db = [];
searched_DEPT_APRT = {};
searched_ARR_APRT = {};
searched_ARL_COD = {};


function addSecs(d, s) {return new Date(d.valueOf()+s*1000);}
function doRun(n) {
	if (n=='undefined'){
		n=1;
	}
    console.log('Processing JS...');
    setTimeout(function(){
         start = new Date();
         end = addSecs(start,n);
         do {start = new Date();} while (end-start > 0);
         console.log('Finished JS');   
    },10);
}

// List of airports
function generateAirportLists(){
	temp = '{"aggs":{"air":{"nested":{"path":"AIR"},"aggs":{"dept_aprt":{"terms":{"field":"AIR.DEPT_APRT","size":10000}},"arr_aprt":{"terms":{"field":"AIR.ARR_APRT","size":10000}},"airlines":{"terms":{"field":"AIR.ARL_COD","size":10000}}}}}}';
	return temp;
}

function getAirportLists(){

	var url = "http://localhost:9200/faa_nextor_traj/_search?size=0"
	var client = new XMLHttpRequest();
	client.open("POST", url, false);
	client.setRequestHeader("Content-Type", "text/plain");
	try {
		client.send(generateAirportLists());
	} catch(err) {
	    alert("Could not fetch the airport list. There is probably a connection problem with the server!\nRemember that you have to port forward cicero's 9200 on your 9200");
	    spinner.stop()
	}
	if (client.status != 200){
		alert('There was an error with your request!\n'+client.statusText);
		spinner.stop()
    } else {
		var obj2 = JSON.parse(client.responseText);
		searched_DEPT_APRT = obj2.aggregations.air.dept_aprt;
		searched_ARR_APRT = obj2.aggregations.air.arr_aprt;
		searched_ARL_COD = obj2.aggregations.air.airlines;

		dept_aprt_in_db = [];
		arr_aprt_in_db = [];
		airlines_in_db = [];
		searched_DEPT_APRT.buckets.forEach(function(d){dept_aprt_in_db.push(d.key)});
		searched_ARR_APRT.buckets.forEach(function(d){arr_aprt_in_db.push(d.key)});
		searched_ARL_COD.buckets.forEach(function(d){airlines_in_db.push(d.key)});
	}
}

function update_form_options(){
	getAirportLists();

	d3.selectAll("#DEPT_APRT").selectAll("option").remove();
	var dept_airport_list = d3.selectAll("#DEPT_APRT");
	dept_airport_list.selectAll("option")
		.data(["Select by Airport          "].concat(dept_aprt_in_db.sort()))
		.enter()
		.append("option")
		.attr("value",function(d){
			if (d.length<=10){return d;
			}else{
				return "";
			}
		})
		.text(function(d){return d;});

	d3.selectAll("#ARR_APRT").selectAll("option").remove();
	var arr_airport_list = d3.selectAll("#ARR_APRT");
	arr_airport_list.selectAll("option")
		.data(["Select by Airport          "].concat(arr_aprt_in_db.sort()))
		.enter()
		.append("option")
		.attr("value",function(d){
			if (d.length<=10){return d;
			}else{
				return "";
			}
		})
		.text(function(d){return d;});

	d3.selectAll("#AirlineCode").selectAll("option").remove();
	var airl_list = d3.selectAll("#AirlineCode");
	airl_list.selectAll("option")
		.data(["Select by Airline          "].concat(airlines_in_db.sort()))
		.enter()
		.append("option")
		.attr("value",function(d){
			if (d.length<=10){return d;
			}else{
				return "";
			}
		})
		.text(function(d){return d;});
}

