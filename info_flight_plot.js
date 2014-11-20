// var dists = [], times = []
function draw_metrics(mflights){
  // console.log(mflights);
  if (mflights !== "undefined" && mflights.length>0)
  {
    //
    var ts_achieved = [];
    var ts_total = [];
    var times = [], dists_achieved = [];dists_total = [];
    mflights.forEach(function(o,i) {
      if (o.metrics.total_dist40to40>0 ){//&& o.metrics.total_dist40to100>0&& o.metrics.total_dist100to100>0&&o.metrics.achieved_dist40to40>0 && o.metrics.achieved_dist40to100>0&& o.metrics.achieved_dist100to100>0){ //do not use the weird points       
        ts_total.push({data:o.metrics.achieved_dist40to40, time:o.metrics.travel_time_40to40, type:"40to40", typecode:1})
        ts_total.push({data:o.metrics.achieved_dist40to100, time:o.metrics.travel_time_40to100, type:"40to100", typecode:2})
        ts_total.push({data:o.metrics.achieved_dist100to100, time:o.metrics.travel_time_100to100, type:"100to100", typecode:3})
        dists_total.push(o.metrics.achieved_dist40to40);
        dists_total.push(o.metrics.achieved_dist40to100);
        dists_total.push(o.metrics.achieved_dist100to100);
        ts_achieved.push({data:o.metrics.total_dist40to40, time:o.metrics.travel_time_40to40, type:"40to40", typecode:1})
        ts_achieved.push({data:o.metrics.total_dist40to100, time:o.metrics.travel_time_40to100, type:"40to100", typecode:2})
        ts_achieved.push({data:o.metrics.total_dist100to100, time:o.metrics.travel_time_100to100, type:"100to100", typecode:3})
        dists_achieved.push(o.metrics.total_dist40to40);
        dists_achieved.push(o.metrics.total_dist40to100);
        dists_achieved.push(o.metrics.total_dist100to100);
        times.push(o.metrics.travel_time_40to40);
        times.push(o.metrics.travel_time_40to100);
        times.push(o.metrics.travel_time_100to100);
		
      }
	  
    });
	
    // ts = ts40to40.concat(ts40to100.concat(ts100to100));
// console.log(dists)
    // //remove the lowest and highest points
    // ts_total=ts_total.sort(function(a, b){return a-b});
    // ts_total=ts_total.slice(1,ts_total.length-1);
    // dists_achieved
	array_achieved_dist40to40 =[];
	array_achieved_dist40to100 =[];
	array_achieved_dist100to100 =[];
	for ( var j = 0; j < dists_achieved.length-3; j = j + 3) { 
		array_achieved_dist40to40.push(dists_achieved[j]);
		array_achieved_dist40to100.push(dists_achieved[j+1]);
		array_achieved_dist100to100.push(dists_achieved[j+2]);
	}
	var avg_achieved_dist40to40 = average(array_achieved_dist40to40);
	var avg_achieved_dist40to100 = average(array_achieved_dist40to100);
	var avg_achieved_dist100to100 = average(array_achieved_dist100to100);
	var stdDev_achieved_dist40to40 = standardDeviation(array_achieved_dist40to40);
	var stdDev_achieved_dist40to100 = standardDeviation(array_achieved_dist40to100);
	var stdDev_achieved_dist100to100 = standardDeviation(array_achieved_dist100to100);
	var Z = 1.645;
	var confidence_achieved_dist40to40 = Z * stdDev_achieved_dist40to40 / Math.sqrt(array_achieved_dist40to40.length - 1);
	var confidence_achieved_dist40to100 = Z * stdDev_achieved_dist40to100 / Math.sqrt(array_achieved_dist40to100.length - 1);
	var confidence_achieved_dist100to100 = Z * stdDev_achieved_dist100to100 / Math.sqrt(array_achieved_dist100to100.length - 1);
	// dists_total
	array_total_dist40to40 =[];
	array_total_dist40to100 =[];
	array_total_dist100to100 =[];
	for ( var j = 0; j < dists_total.length-3; j = j + 3) { 
		array_total_dist40to40.push(dists_total[j]);
		array_total_dist40to100.push(dists_total[j+1]);
		array_total_dist100to100.push(dists_total[j+2]);
	}
	var avg_total_dist40to40 = average(array_total_dist40to40);
	var avg_total_dist40to100 = average(array_total_dist40to100);
	var avg_total_dist100to100 = average(array_total_dist100to100);
	var stdDev_total_dist40to40 = standardDeviation(array_total_dist40to40);
	var stdDev_total_dist40to100 = standardDeviation(array_total_dist40to100);
	var stdDev_total_dist100to100 = standardDeviation(array_total_dist100to100);
	var confidence_total_dist40to40 = Z * stdDev_total_dist40to40 / Math.sqrt(array_total_dist40to40.length - 1);
	var confidence_total_dist40to100 = Z * stdDev_total_dist40to100 / Math.sqrt(array_total_dist40to100.length - 1);
	var confidence_total_dist100to100 = Z * stdDev_total_dist100to100 / Math.sqrt(array_total_dist100to100.length - 1);
	// times
	array_times40to40 =[];
	array_times40to100 =[];
	array_times100to100 =[];
	for ( var j = 0; j < times.length-3; j = j + 3) { 
		array_times40to40.push(times[j]);
		array_times40to100.push(times[j+1]);
		array_times100to100.push(times[j+2]);
	}
	var avg_times40to40 = average(array_times40to40);
	var avg_times40to100 = average(array_times40to100);
	var avg_times100to100 = average(array_times100to100);
	var stdDev_times40to40 = standardDeviation(array_times40to40);
	var stdDev_times40to100 = standardDeviation(array_times40to100);
	var stdDev_times100to100 = standardDeviation(array_times100to100);
	var confidence_times40to40 = Z * stdDev_times40to40 / Math.sqrt(array_times40to40.length - 1);
	var confidence_times40to100 = Z * stdDev_times40to100 / Math.sqrt(array_times40to100.length - 1);
	var confidence_times100to100 = Z * stdDev_times100to100 / Math.sqrt(array_times100to100.length - 1);
// getting rid of outlier 
	var ts_achieved2 = [];
	dists_achieved2 = [];
	var ts_total2 = [];
	dists_total2 = [];
	times2=[];
	/*for (var index = 0; index < array_achieved_dist40to40.length; index++){
		if (array_achieved_dist40to40[index] > 0.6*avg_achieved_dist40to40){
			ts_achieved2.push({data:array_achieved_dist40to40[index], time:array_times40to40[index], type:"40to40", typecode:1});
			ts_achieved2.push({data:array_achieved_dist40to100[index], time:array_times40to100[index], type:"40to100", typecode:2});
			ts_achieved2.push({data:array_achieved_dist100to100[index], time:array_times100to100[index], type:"100to100", typecode:3});
			dists_achieved2.push(array_achieved_dist40to40[index]);
			dists_achieved2.push(array_achieved_dist40to100[index]);
			dists_achieved2.push(array_achieved_dist100to100[index]);
		}
	}*/

	for (var index = 0; index < array_total_dist40to40.length; index++){
		if (array_total_dist40to40[index] > 0.6*avg_total_dist40to40){
		//&&array_total_dist40to100[index] > 0.6*avg_total_dist40to100
		//&&array_total_dist100to100[index] > 0.6*avg_total_dist100to100){
			ts_total2.push({data:array_total_dist40to40[index], time:array_times40to40[index], type:"40to40", typecode:1});
			ts_total2.push({data:array_total_dist40to100[index], time:array_times40to100[index], type:"40to100", typecode:2});
			ts_total2.push({data:array_total_dist100to100[index], time:array_times100to100[index], type:"100to100", typecode:3});
			dists_total2.push(array_total_dist40to40[index]);
			dists_total2.push(array_total_dist40to100[index]);
			dists_total2.push(array_total_dist100to100[index]);
			ts_achieved2.push({data:array_achieved_dist40to40[index], time:array_times40to40[index], type:"40to40", typecode:1});
			ts_achieved2.push({data:array_achieved_dist40to100[index], time:array_times40to100[index], type:"40to100", typecode:2});
			ts_achieved2.push({data:array_achieved_dist100to100[index], time:array_times100to100[index], type:"100to100", typecode:3});
			dists_achieved2.push(array_achieved_dist40to40[index]);
			dists_achieved2.push(array_achieved_dist40to100[index]);
			dists_achieved2.push(array_achieved_dist100to100[index]);
			times2.push(array_times40to40[index]);
			times2.push(array_times40to100[index]);
			times2.push(array_times100to100[index]);
		}
	}
	plot_metric_one_figure(ts_achieved2,[d3.min(dists_achieved2), d3.max(dists_achieved2)],[d3.min(times2), d3.max(times2)],"#flighttime_vs_achieved_distance",["40 to 40 NM","40 to 100 NM","100 to 100 NM"])
    plot_metric_one_figure(ts_total2,[d3.min(dists_total2), d3.max(dists_total2)],[d3.min(times2), d3.max(times2)],"#flighttime_vs_total_distance",["40 to 40 NM","40 to 100 NM","100 to 100 NM"])
	plot_stat_table((avg_achieved_dist40to40),(avg_achieved_dist40to100),(avg_achieved_dist100to100),(stdDev_achieved_dist40to40),(stdDev_achieved_dist40to100),(stdDev_achieved_dist100to100),(confidence_achieved_dist40to40),(confidence_achieved_dist40to100),(confidence_achieved_dist100to100),(avg_total_dist40to40),(avg_total_dist40to100),(avg_total_dist100to100),(stdDev_total_dist40to40),(stdDev_total_dist40to100),(stdDev_total_dist100to100),(confidence_total_dist40to40),(confidence_total_dist40to100),(confidence_total_dist100to100),(avg_times40to40),(avg_times40to100),(avg_times100to100),(stdDev_times40to40),(stdDev_times40to100),(stdDev_times100to100),(confidence_times40to40),(confidence_times40to100),(confidence_times100to100))   
	}
}
function plot_stat_table(t11,t21,t31,t12,t22,t32,t13,t23,t33,t14,t24,t34,t15,t25,t35,t16,t26,t36,t17,t27,t37,t18,t28,t38,t19,t29,t39){
	var x = document.getElementById("myStats").rows[2].cells;
	var y = document.getElementById("myStats").rows[3].cells;
	var z = document.getElementById("myStats").rows[4].cells;
    x[1].innerHTML = Math.round(t11* 100) / 100;
	x[2].innerHTML = Math.round(t12* 100) / 100;
	x[3].innerHTML = Math.round(t13* 100) / 100;
	x[4].innerHTML = Math.round(t14* 100) / 100;
	x[5].innerHTML = Math.round(t15* 100) / 100;
	x[6].innerHTML = Math.round(t16* 100) / 100;
	x[7].innerHTML = Math.round(t17* 100) / 100;
	x[8].innerHTML = Math.round(t18* 100) / 100;
	x[9].innerHTML = Math.round(t19* 100) / 100;
	
	y[1].innerHTML = Math.round(t21* 100) / 100;
	y[2].innerHTML = Math.round(t22* 100) / 100;
	y[3].innerHTML = Math.round(t23* 100) / 100;
	y[4].innerHTML = Math.round(t24* 100) / 100;
	y[5].innerHTML = Math.round(t25* 100) / 100;
	y[6].innerHTML = Math.round(t26* 100) / 100;
	y[7].innerHTML = Math.round(t27* 100) / 100;
	y[8].innerHTML = Math.round(t28* 100) / 100;
	y[9].innerHTML = Math.round(t29* 100) / 100;
	
	z[1].innerHTML = Math.round(t31* 100) / 100;
	z[2].innerHTML = Math.round(t32* 100) / 100;
	z[3].innerHTML = Math.round(t33* 100) / 100;
	z[4].innerHTML = Math.round(t34* 100) / 100;
	z[5].innerHTML = Math.round(t35* 100) / 100;
	z[6].innerHTML = Math.round(t36* 100) / 100;
	z[7].innerHTML = Math.round(t37* 100) / 100;
	z[8].innerHTML = Math.round(t38* 100) / 100;
	z[9].innerHTML = Math.round(t39* 100) / 100;
}
function standardDeviation(values){
  var avg = average(values);
  
  var squareDiffs = values.map(function(value){
    var diff = value - avg;
    var sqrDiff = diff * diff;
    return sqrDiff;
  });
  
  var avgSquareDiff = average(squareDiffs);
 
  var stdDev = Math.sqrt(avgSquareDiff);
  return stdDev;
}
 
function average(data){
  var sum = data.reduce(function(sum, value){
    return sum + value;
  }, 0);
 
  var avg = sum / data.length;
  return avg;
}

function plot_metric_one_figure(ts,xdomain,ydomain,figure_name,legend_name){
  var color = d3.scale.category10();//like colormap in matlab - 10 elements here
  var size = {
    height: 200,
    width: 840
  }
  var rightOffset = 40, topOffset = 20;

  // create scale to convert values for x and y into pixels
  var scale = {
    x: d3.scale.linear().domain(xdomain)
        .rangeRound([0, size.width-50]),
    y: d3.scale.linear().domain(ydomain)
        .range([size.height, 15])        
  }
    
  // select all figures in <div id="flighttime_vs_distance"> and delete them
  d3.selectAll(figure_name).selectAll('svg').remove();
  var chart = d3.selectAll(figure_name)
    .style("display",null) // if was hidden, create figure
    .append('svg:svg') // add figure inside div
    .data(ts) // add data to figure (doesnt know what to do with it yet)
    .attr('width', size.width+rightOffset) // stipulate figure size
    .attr('height', size.height+50)
    .append('svg:g'); // tell js that the data will be displayed as "g" elements

  chart.selectAll('circle.dot') // select all dots in figure
    .data(ts) //replace dots data with ts data
    .enter().append('svg:circle') // create new dots with ts
    .attr('class', 'dot') // stipulate that they are to beplotted as dots
    .attr('cx', function(o, i){return scale.x(o.data)+rightOffset;}) // and should be plotted with center at (cx,cy) in pixels
    .attr('cy', function(o, i){return scale.y(o.time)+topOffset;})
    .attr('r', 1.5)
    .style("fill", function(d){ return color(d.typecode);}) // and filled with color depending on typecode

  // create x,y axis
  var xAxis = d3.svg.axis()
    .scale(scale.x)
    .orient('bottom')
  var yAxis = d3.svg.axis()
    .scale(scale.y)
    .orient("left");

  // create label for (x,y) axis
  chart.append("g")
    .attr("class", "axis")
    .attr("transform", "translate("+ rightOffset+","+(200+topOffset)+")")
    .call(xAxis);
  chart.append("g")
    .attr("class", "axis")
    .attr("transform", "translate("+ rightOffset+","+topOffset+")")
    .call(yAxis);

    // create legend
  typename = legend_name;
  var legend = chart.selectAll(".legend")
      .data(color.domain())
      .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(-10," + (50+(i * 20)) + ")"; });

  // create color rectangles for legend
  legend.append("rect")
      .attr("x", size.width - 18)
      .attr("width", 6)
      .attr("height", 6)
      .style("fill", color);
  // add text next to rectangle for legend
  legend.append("text")
      .attr("x", size.width - 24)
      .attr("y", 9)
      .attr("dy", ".10em")
      .style("text-anchor", "end")
      .text(function(d,i) { return typename[i]; });

  }
function plot_altitude(d){
    var ts = []
    d.properties.POSIT_DATE.forEach(function(o,i) {
      ts.push({data:d.geometry.altitude[i], time:d.geometry.times[i]})
    });

  var size = {
    height: 200,
    width: 840
  }
  var rightOffset = 40, topOffset = 20;

  var scale = {
    x: d3.time.scale().domain([ts[0].time, ts[ts.length - 1].time])
        .rangeRound([0, size.width]),
    y: d3.scale.linear().domain([0, d3.max(d.geometry.altitude)]).range([size.height, 15])        
  }
    
  d3.selectAll('#altitude_plot').selectAll('svg').remove();
  var chart = d3.selectAll('#altitude_plot')
    .append('svg:svg')
    .data(ts)
    .attr('width', size.width+rightOffset)
    .attr('height', size.height+50)
    .append('svg:g');

  var line = d3.svg.area()
    .x(function(o, i){return scale.x(o.time);})
    .y(function(o, i){return scale.y(o.data);})
    .y0(size.height)
    .interpolate("cardinal");

  chart.append('path')
    // .on("mouseenter", function(d) {
    //   console.log('coucou');
    //     d=d.properties;
    //     var titleHtml = d.DEPT_APRT + " -> " + d.ARR_APRT + "</br>";
    //     titleHtml += d.ARL_COD + d.FLI_NUM + "</br>";

    //     var contentHtml = "";
    //     contentHtml += datetimeformat.parse(d.ORIG_DATE+"T"+d.ORIG_TIME)+"</br>";
    //     contentHtml += "Tail: " + d.BEACON_CODE +"</br></br>";
    //     contentHtml += "Scheduled: " + 'xxxx' +"-"+'xxxx' +"</br>";
    //     contentHtml += "Actual: " + 'xxxx' +"-"+'xxxx' +"</br>";

    //     e = d3.event;
    //     var p = d3.select('#alt-pop-up');

    //     var pl = e.pageX + 50;
    //     var pt = e.pageY - 25;
        
    //     p.style('left', '40px')
    //      .style('top', '60%');

    //     d3.select('#alt-pop-up-title').html(titleHtml);
    //     d3.select('#altpop-up-content').html(contentHtml);

    //     d3.select('#alt-pop-up')
    //       .transition()
    //       .style('opacity', 100)
    //       .style('display', 'block')
    //       .duration(3000);

    //     if (popupTimer) {
    //       clearTimeout(popupTimer);
    //     }

    //     popupTimer = setTimeout(fade_out_popup, 5000);
    //   })
    .attr('d', line(ts))
    .attr("stroke", "#006699")
    .attr("stroke-width", 1)
    .style("fill-opacity", .1)
    .attr("fill", "#006699")
    .attr("transform", "translate("+ rightOffset+","+topOffset+")");

  chart.selectAll('circle.mark')
    .data(ts).enter().append('svg:circle')
    .attr('class', 'mark')
    .attr('cx', function(o, i){return scale.x(o.time)+rightOffset;})
    .attr('cy', function(o, i){return scale.y(o.data)+topOffset;})
    .attr('r', 2.5)

  var xAxis = d3.svg.axis()
    .scale(scale.x)
    .orient('bottom')
    .ticks(d3.time.minute, 30)
    .tickFormat(d3.time.format('%H:%M'))
    .tickPadding(5);
    // .tickFormat(d3.time.format('%H:%M'))
    // .tickSize(5)
    // .tickPadding(8);
  var yAxis = d3.svg.axis()
    .scale(scale.y)
    .orient("left");

  chart.append("g")
    .attr("class", "axis")
    .attr("transform", "translate("+ rightOffset+","+(200+topOffset)+")")
    .call(xAxis);
  chart.append("g")
    .attr("class", "axis")
    .attr("transform", "translate("+ rightOffset+","+topOffset+")")
    .call(yAxis);
}



function plot_groundspeed(d){
    var ts = []
    d.properties.POSIT_DATE.forEach(function(o,i) {
      ts.push({data:d.geometry.groundspeed[i], time:d.geometry.times[i]})
    });

  var size = {
    height: 200,
    width: 840
  }
  var rightOffset = 40, topOffset = 20;

  var scale = {
        x: d3.time.scale().domain([ts[0].time, ts[ts.length - 1].time])
        .rangeRound([0, size.width]),
    y: d3.scale.linear().domain([0, d3.max(d.geometry.groundspeed)]).range([size.height, 15])        
  }
    
  d3.selectAll('#groundspeed_plot').selectAll('svg').remove();
  var chart = d3.selectAll('#groundspeed_plot')
    .append('svg:svg')
    .data(ts)
    .attr('width', size.width+rightOffset)
    .attr('height', size.height+50)
    .append('svg:g');

  var line = d3.svg.area()
    .x(function(o, i){return scale.x(o.time);})
    .y(function(o, i){return scale.y(o.data);})
    .y0(size.height)
    .interpolate("cardinal");

  chart.append('path')
    .attr('d', line(ts))
    .attr("stroke", "#006699")
    .attr("stroke-width", 1)
    .style("fill-opacity", .1)
    .attr("fill", "#006699")
    .attr("transform", "translate("+ rightOffset+","+topOffset+")");

  chart.selectAll('circle.mark')
    .data(ts).enter().append('svg:circle')
    // .on("mouseenter", function(d) {
    //     popup_create2(d.properties);reset_popup_timer();
    //   })
    .attr('class', 'mark')
    .attr('cx', function(o, i){return scale.x(o.time)+rightOffset;})
    .attr('cy', function(o, i){return scale.y(o.data)+topOffset;})
    .attr('r', 2.5)

  var xAxis = d3.svg.axis()
    .scale(scale.x)
    .orient("bottom")
    .ticks(d3.time.minutes, 30)
    .tickFormat(d3.time.format('%H:%M'))
    // .tickSize(5)
    // .tickPadding(8);
  var yAxis = d3.svg.axis()
    .scale(scale.y)
    .orient("left");

  chart.append("g")
    .attr("class", "axis")
    .attr("transform", "translate("+ rightOffset+","+(200+topOffset)+")")
    .call(xAxis);
  chart.append("g")
    .attr("class", "axis")
    .attr("transform", "translate("+ rightOffset+","+topOffset+")")
    .call(yAxis);
  // chart.append("g")
  //   .attr("class","legend")
  //   .attr("transform","translate(50,30)")
  //   .call(d3.legend);
}