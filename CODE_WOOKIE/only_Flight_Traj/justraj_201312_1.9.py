import json
import csv
from datetime import datetime


fid = open('TZ_CP_201309_12.csv','rb')
#fid = open('traj_test.csv','rb')
r, n = 0, 0
acid = ''
temp2 = []
acList = []
cidList = []
uniqueList = []
fixtime=0
fixtime2=0
for row in fid:
	row = row.replace('\r\n','')
	row = row.replace('"','')
	if r == 0:
		field = row.split(',')
		r += 1
	else:
		temp1 = row.split(',')
		if temp1[3][3:5] in 'DEC':
			if acid == '' or (temp1[2] +'_'+temp1[3] +'_'+temp1[4]) not in uniqueList:
				temp2.append({})
				uniqueList.append(temp1[2] +'_'+temp1[3] +'_'+temp1[4])
				acList.append(temp1[2])
				cidList.append(temp1[4])
				index = len(uniqueList)-1				
				temp2[index]["AIR"] = []
				temp2[index]["POSITION"] = []
				temp2[index]["LOCATION"] = []
				temp2[index]["AIR"].append({})
				temp2[index]["POSITION"].append({})
				temp2[index]["LOCATION"].append({})
				acid = temp1[2]
				cid = temp1[4]
############### beginning plan
############### end plan
				
				for i in range(0, len(field)):
					if i not in [0,2,5,6,7,8,9,10,11]:
						temp2[index]["AIR"][0][field[i]] = temp1[i]
					if i in [0]:
						temp2[index]["AIR"][0]['DEP_APRT'] = temp1[i]
					if i in [2]:
						temp2[index]["AIR"][0]['ARL_COD'] = temp1[i][0:3]
						temp2[index]["AIR"][0]['FLI_NUM'] = temp1[i][3::]
					if i in [5]:
							fixtime = datetime.strptime(temp1[i],'%Y%m%d %H:%M:%S')
							temp2[index]["AIR"][0]['ORIG_DATE'] = fixtime.strftime('%Y%m%d %H:%M:%S')[0:8]
							temp2[index]["AIR"][0]['ORIG_TIME'] = fixtime.strftime('%Y%m%d %H:%M:%S')[9::]
					if i in [6]:
							fixtime2 = datetime.strptime(temp1[i],'%Y%m%d %H:%M:%S')
							temp2[index]["AIR"][0]['ARR_EST_DATE'] = fixtime2.strftime('%Y%m%d %H:%M:%S')[0:8]
							temp2[index]["AIR"][0]['ARR_EST_TIME'] = fixtime2.strftime('%Y%m%d %H:%M:%S')[9::]
					if i in [7]:
						temp2[index]["AIR"][0]['POSIT_DATE'] = []
						temp2[index]["AIR"][0]['POSIT_TIME'] = []
						temp2[index]["AIR"][0]['POSIT_DATE'].append(temp1[i][0:8])
						temp2[index]["AIR"][0]['POSIT_TIME'].append(temp1[i][9::])
					if i in[8]:
						temp2[index]["LOCATION"][0]['type'] = 'linestring'
						temp2[index]["LOCATION"][0]['coordinates'] = []
						temp2[index]["LOCATION"][0]['coordinates'].append([((float(temp1[i+1]))),(float(temp1[i]))])
					if i in [9]:
						temp3=[]
					if i in [10,11]:
						temp2[index]["POSITION"][0][field[i]] = []
						temp2[index]["POSITION"][0][field[i]].append(float(temp1[i]))
				n += 1
			else:
				index = uniqueList.index(temp1[2] +'_'+temp1[3] +'_'+temp1[4])
				fixtime = datetime.strptime(temp2[index]["AIR"][0]['ORIG_DATE'] + ' ' + temp2[index]["AIR"][0]['ORIG_TIME'],'%Y%m%d %H:%M:%S')
				fixtime2 = datetime.strptime(temp2[index]["AIR"][0]['ARR_EST_DATE'] + ' ' + temp2[index]["AIR"][0]['ARR_EST_TIME'],'%Y%m%d %H:%M:%S')
				fixtime_arr = datetime.strptime(temp2[index]["AIR"][0]['ORIG_DATE'] + ' ' + temp2[index]["AIR"][0]['ORIG_TIME'],'%Y%m%d %H:%M:%S')
				if fixtime > datetime.strptime(temp1[5],'%Y%m%d %H:%M:%S'):
					fixtime = datetime.strptime(temp1[5],'%Y%m%d %H:%M:%S')
					temp2[index]["AIR"][0]['ORIG_DATE'] = fixtime.strftime('%Y%m%d %H:%M:%S')[0:8]
					temp2[index]["AIR"][0]['ORIG_TIME'] = fixtime.strftime('%Y%m%d %H:%M:%S')[9::]
					
				elif fixtime < datetime.strptime(temp1[5],'%Y%m%d %H:%M:%S'):
					fixtime = fixtime
					temp2[index]["AIR"][0]['ORIG_DATE'] = fixtime.strftime('%Y%m%d %H:%M:%S')[0:8]
					temp2[index]["AIR"][0]['ORIG_TIME'] = fixtime.strftime('%Y%m%d %H:%M:%S')[9::]
					
				if fixtime_arr > datetime.strptime(temp1[5],'%Y%m%d %H:%M:%S'):
					fixtime2 = fixtime2
					temp2[index]["AIR"][0]['ARR_EST_DATE'] = fixtime2.strftime('%Y%m%d %H:%M:%S')[0:8]
					temp2[index]["AIR"][0]['ARR_EST_TIME'] = fixtime2.strftime('%Y%m%d %H:%M:%S')[9::]
				elif fixtime_arr < datetime.strptime(temp1[5],'%Y%m%d %H:%M:%S'):
					fixtime2 = datetime.strptime(temp1[6],'%Y%m%d %H:%M:%S')
					temp2[index]["AIR"][0]['ARR_EST_DATE'] = fixtime2.strftime('%Y%m%d %H:%M:%S')[0:8]
					temp2[index]["AIR"][0]['ARR_EST_TIME'] = fixtime2.strftime('%Y%m%d %H:%M:%S')[9::]
				temp2[index]["LOCATION"][0]['coordinates'].append([((float(temp1[9]))),(float(temp1[8]))])
				temp2[index]["POSITION"][0]['GROUNDSPEED'].append(float(temp1[10]))
				temp2[index]["POSITION"][0]['ALTITUDE'].append(float(temp1[11]))
				temp2[index]["AIR"][0]['POSIT_DATE'].append(temp1[7][0:8])
				temp2[index]["AIR"][0]['POSIT_TIME'].append(temp1[7][9::])
				
		else:
			n1='not JAN'
for i, item in enumerate(temp2):
	item = str(item).replace('\'','\"')
	json = open(uniqueList[i]+'.json', 'wb')
	json.write(item)
	json.close()			

fid.close()