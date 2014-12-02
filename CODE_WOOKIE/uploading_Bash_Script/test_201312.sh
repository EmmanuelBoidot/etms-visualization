#!/bin/bash
i=296048
for entry in *
do
	if [[ ${entry: -5} == ".json" ]]; then
		#curl -XPOST "http://localhost:9200/ironman/test/$i" -d @$entry
		curl -XPOST "http://128.61.186.135:9200/faa_nextor_flight_traj_plan/test/$i" -d @$entry
		let i+=1
		echo $entry
	fi
done