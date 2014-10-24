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