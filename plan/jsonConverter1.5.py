import json
import csv

fid = open('FLIGHT_PLAN_EN_CP_2014_part3.csv', 'rb')
# fid = open('test.csv','rb')
r, n = 0, 0
for row in fid:
	row = row.replace('\r\n', '')
	row = row.replace('"', '')
	if r == 0:
		field = row.split(',')
		r += 1
	else:
		temp2 = {}
		temp2["AIR"] = []
		temp2["POSITION"] = []
		temp2["LOCATION"] = []
		temp2["AIR"].append({})
		temp2["POSITION"].append({})
		temp2["POSITION"][0]['ALTITUDE']=[]
		temp2["LOCATION"].append({})
		temp1 = row.split(',')
# ORIG 0-68
		date = temp1[0]
		acid = temp1[1]
		temp2["AIR"][0]['ACT_DATE'] = temp1[0]
		temp2["AIR"][0]['ARL_COD'] = acid[0:3]
		temp2["AIR"][0]['FLI_NUM'] = acid[3::]
		temp2["AIR"][0]['FLIGHT_INDEX'] = temp1[2]
		temp2["AIR"][0]['DEP_ARPT'] = temp1[3]
		ARR_APRT = temp1[4]
		D40_coord = [-float(temp1[6])/60, float(temp1[5])/60]
		D40_alt = temp1[7]
		temp2["POSITION"][0]['ALTITUDE'].append(D40_alt)
		D40_time = temp1[8]
		D100_coord = [-float(temp1[15])/60, float(temp1[14])/60]
		D100_alt = temp1[16]
		temp2["POSITION"][0]['ALTITUDE'].append(D100_alt)
		D100_time = temp1[17]
		if temp1[24]!= '' and temp1[23] != '':
			A200_coord = [-float(temp1[24])/60, float(temp1[23])/60]
		else:
			A200_coord =''	
		A200_alt = temp1[25]
		
		temp2["POSITION"][0]['ALTITUDE'].append(temp1[57])
		
		temp2["POSITION"][0]['ALTITUDE'].append(A200_alt)
		A200_time = temp1[26]
		A100_coord = [-float(temp1[33])/60,float(temp1[32])/60]
		A100_alt = temp1[34]
		temp2["POSITION"][0]['ALTITUDE'].append(A100_alt)
		A100_time = temp1[35]
		A40_coord = [-float(temp1[42])/60,float(temp1[41])/60]
		A40_alt = temp1[43]
		temp2["POSITION"][0]['ALTITUDE'].append(A40_alt)
		A40_time = temp1[44]
		temp2["POSITION"][0]['D40_TIME']=(D40_time)[9::]
		temp2["POSITION"][0]['D100_TIME']=(D100_time)[9::]
		temp2["POSITION"][0]['A200_TIME']=(A200_time)[9::]
		temp2["POSITION"][0]['A100_TIME']=(A100_time)[9::]
		temp2["POSITION"][0]['A40_TIME']=(A40_time)[9::]
		temp2["POSITION"][0]['D40_DATE']=(D40_time)[0:8]
		temp2["POSITION"][0]['D100_DATE']=(D100_time)[0:8]
		temp2["POSITION"][0]['A200_DATE']=(A200_time)[0:8]
		temp2["POSITION"][0]['A100_DATE']=(A100_time)[0:8]
		temp2["POSITION"][0]['A40_DATE']=(A40_time)[0:8]
		
		#ARR_TIME = temp1[50]
		temp2["AIR"][0]['ARR_TIME'] = temp1[50][9::]
		temp2["AIR"][0]['ARR_DATE'] = temp1[50][0:8]
		#FP_DEPT_TIME = temp1[55]
		temp2["AIR"][0]['FP_DEPT_TIME'] = temp1[55][9::]
		temp2["AIR"][0]['FP_DEPT_DATE'] = temp1[55][0:8]
		#FP_ARR_TIME = temp1[56]
		temp2["AIR"][0]['FP_ARR_TIME'] = temp1[56][9::]
		temp2["AIR"][0]['FP_ARR_DATE'] = temp1[56][0:8]
		
		temp2["AIR"][0]['ACTUAL_ARR_TIME'] = temp1[65][9::]
		temp2["AIR"][0]['SCHED_DEP_DATE'] = temp1[62][0:8]
		
		temp2["POSITION"][0]['SPEED'] = temp1[58]
		temp2["AIR"][0]['ACFT_TYPE'] = temp1[59]
		temp2["AIR"][0]['SCHED_DEP_TIME'] = temp1[62][9::]
		temp2["AIR"][0]['SCHED_ARR_TIME'] = temp1[63][9::]
		temp2["AIR"][0]['ACTUAL_DEP_TIME'] = temp1[64][9::]
		temp2["AIR"][0]['ACTUAL_ARR_TIME'] = temp1[65][9::]
		temp2["AIR"][0]['SCHED_DEP_DATE'] = temp1[62][0:8]
		temp2["AIR"][0]['SCHED_ARR_DATE'] = temp1[63][0:8]
		temp2["AIR"][0]['ACTUAL_DEP_DATE'] = temp1[64][0:8]
		temp2["AIR"][0]['ACTUAL_ARR_DATE'] = temp1[65][0:8]
		
# working on LF 69-98
		LF_ARR_APRT = temp1[70]
		if temp1[76] != '' and temp1[77] != '' and temp1[79] != '' and temp1[80] != '' and temp1[84] != '' and temp1[85] != '' and temp1[89] != '' and temp1[90] != '' and temp1[94] != '' and temp1[95] != '':
			LF_DEP_coord = [-float(temp1[77])/60, float(temp1[76])/60]
			LF_D40_coord = [-float(temp1[80])/60, float(temp1[79])/60]
			LF_A100_coord = [-float(temp1[85])/60,float(temp1[84])/60]
			LF_A40_coord = [-float(temp1[90])/60,float(temp1[89])/60]
			LF_ARR_coord = [-float(temp1[95])/60,float(temp1[94])/60]
		LF_WAYPT = temp1[71]
		LF_FPWAYPT = temp1[72][1::]		
# working on PD 99-128
		PD_ARR_APRT = temp1[100]
		if temp1[106] != '' and temp1[107] != '' and temp1[109] != '' and temp1[110] != '' and temp1[114] != '' and temp1[115] != '' and temp1[119] != '' and temp1[120] != '' and temp1[124] != '' and temp1[125] != '':
			PD_DEP_coord = [-float(temp1[107])/60, float(temp1[106])/60]
			PD_D40_coord = [-float(temp1[110])/60, float(temp1[109])/60]
			PD_A100_coord = [-float(temp1[115])/60,float(temp1[114])/60]
			PD_A40_coord = [-float(temp1[120])/60,float(temp1[119])/60]
			PD_ARR_coord = [-float(temp1[125])/60,float(temp1[124])/60]
		PD_WAYPT = temp1[101]
		PD_FPWAYPT = temp1[102][1::]

# working on LA 129-158
		#temp2["AIR"][0]['ARR_APRT'] = temp1[130]	
		LA_ARR_APRT = temp1[130]
		if temp1[136] != '' and temp1[137] != '' and temp1[139] != '' and temp1[140] != '' and temp1[144] != '' and temp1[145] != '' and temp1[149] != '' and temp1[150] != '' and temp1[154] != '' and temp1[155] != '':
			LA_DEP_coord = [-float(temp1[137])/60, float(temp1[136])/60]
			LA_D40_coord = [-float(temp1[140])/60, float(temp1[139])/60]
			LA_A100_coord = [-float(temp1[145])/60,float(temp1[144])/60]
			LA_A40_coord = [-float(temp1[150])/60,float(temp1[149])/60]		
			LA_ARR_coord = [-float(temp1[155])/60,float(temp1[154])/60]
		LA_WAYPT = temp1[131]
		LA_FPWAYPT = temp1[132][1::]

# matching it up
		if ARR_APRT != LF_ARR_APRT or ARR_APRT != PD_ARR_APRT or  ARR_APRT != LA_ARR_APRT:
			if LA_ARR_APRT != '':
				final_ARR_APRT = LA_ARR_APRT
			elif LA_ARR_APRT == '' and PD_ARR_APRT != '':
				final_ARR_APRT = PD_ARR_APRT
			elif LA_ARR_APRT == '' and PD_ARR_APRT == '' and LF_ARR_APRT != '':
				final_ARR_APRT = LF_ARR_APRT
		else:
			final_ARR_APRT = ARR_APRT
		temp2["AIR"][0]['ARR_APRT'] = final_ARR_APRT		
		if LF_DEP_coord != PD_DEP_coord or  LF_DEP_coord != LA_DEP_coord:
			if LA_DEP_coord != '':
				final_DEP_coord = LA_DEP_coord
			elif LA_DEP_coord == '' and PD_DEP_coord != '':
				final_DEP_coord = PD_DEP_coord
			elif LA_DEP_coord == '' and PD_DEP_coord == '' and LF_DEP_coord != '':
				final_DEP_coord = LF_DEP_coord
		else:
			final_DEP_coord = LF_DEP_coord
		temp2["AIR"][0]['DEP_coord'] = final_DEP_coord
		if D40_coord != LF_D40_coord or D40_coord != PD_D40_coord or  D40_coord != LA_D40_coord:
			if LA_D40_coord != '':
				final_D40_coord = LA_D40_coord
			elif LA_D40_coord == '' and PD_D40_coord != '':
				final_D40_coord = PD_D40_coord
			elif LA_D40_coord == '' and PD_D40_coord == '' and LF_D40_coord != '':
				final_D40_coord = LF_D40_coord
		else:
			final_D40_coord = D40_coord
		temp2["AIR"][0]['D40_coord'] = final_D40_coord
		
		
		if A100_coord != LF_A100_coord or A100_coord != PD_A100_coord or  A100_coord != LA_A100_coord:
			if LA_A100_coord != '':
				final_A100_coord = LA_A100_coord
			elif LA_A100_coord == '' and PD_A100_coord != '':
				final_A100_coord = PD_A100_coord
			elif LA_A100_coord == '' and PD_A100_coord == '' and LF_A100_coord != '':
				final_A100_coord = LF_A100_coord
		else:
			final_A100_coord = A100_coord
		temp2["AIR"][0]['A100_coord'] = final_A100_coord
		if A40_coord != LF_A40_coord or A40_coord != PD_A40_coord or  A40_coord != LA_A40_coord:
			if LA_A40_coord != '':
				final_A40_coord = LA_A40_coord
			elif LA_A40_coord == '' and PD_A40_coord != '':
				final_A40_coord = PD_A40_coord
			elif LA_A40_coord == '' and PD_A40_coord == '' and LF_A40_coord != '':
				final_A40_coord = LF_A40_coord
		else:
			final_A40_coord = A40_coord
		temp2["AIR"][0]['A40_coord'] = final_A40_coord
		if LF_WAYPT != PD_WAYPT or  LF_WAYPT != LA_WAYPT:
			if LA_WAYPT != '':
				final_WAYPT = LA_WAYPT
			elif LA_WAYPT == '' and PD_WAYPT != '':
				final_WAYPT = PD_WAYPT
			elif LA_WAYPT == '' and PD_WAYPT == '' and LF_WAYPT != '':
				final_WAYPT = LF_WAYPT
		else:
			final_WAYPT = LF_WAYPT
		if LF_FPWAYPT != PD_FPWAYPT or  LF_FPWAYPT != LA_FPWAYPT:
			if LA_FPWAYPT != '':
				final_FPWAYPT = LA_FPWAYPT
			elif LA_FPWAYPT == '' and PD_FPWAYPT != '':
				final_FPWAYPT = PD_FPWAYPT
			elif LA_FPWAYPT == '' and PD_FPWAYPT == '' and LF_FPWAYPT != '':
				final_FPWAYPT = LF_FPWAYPT
		else:
			final_FPWAYPT = LF_FPWAYPT
		if LF_ARR_coord != PD_ARR_coord or  LF_ARR_coord != LA_ARR_coord:
			if LA_ARR_coord != '':
				final_ARR_coord = LA_ARR_coord
			elif LA_ARR_coord == '' and PD_ARR_coord != '':
				final_ARR_coord = PD_ARR_coord
			elif LA_ARR_coord == '' and PD_ARR_coord == '' and LF_ARR_coord != '':
				final_ARR_coord = LF_ARR_coord
		else:
			final_ARR_coord = LF_ARR_coord
		temp2["AIR"][0]['ARR_coord'] = final_ARR_coord
		fpwaypt_coord = final_FPWAYPT.split(' ')
		waypt_coord = final_WAYPT.split(' ')
		temp2["LOCATION"][0]['type'] = 'linestring'
		temp2["LOCATION"][0]['coordinates'] = []
		if final_FPWAYPT!= '':
			for i in range(0, len(fpwaypt_coord)):
				temp2["LOCATION"][0]['coordinates'].append([(-(float(fpwaypt_coord[i][5:9])/60)),(float(fpwaypt_coord[i][0:4])/60)])
		else:
			temp2["LOCATION"][0]['coordinates'].append(fpwaypt_coord)
		#temp2["LOCATION"][0]['type'] = 'linestring'
		#temp2["LOCATION"][0]['coordinates'] = []
		#for i in range(0, len(waypt_coord)):
		#	temp2["LOCATION"][0]['coordinates'].append([(-(float(waypt_coord[i][5:9])/60)),(float(waypt_coord[i][0:4])/60)])
		print acid, date
		temp2 = str(temp2).replace('\'','\"')
		json = open(acid+'_'+date+'_'+temp1[2]+'.json', 'wb')
		json.write(temp2)
		json.close()
fid.close()

#		if acid == '' or (temp1[0] +'_'+temp1[1] +'_'+temp1[2]) not in uniqueList:
#			temp2.append({})
#			uniqueList.append(temp1[0] +'_'+temp1[1] +'_'+temp1[2])
#			index = len(uniqueList)-1
#
#			temp2[index]["AIR"] = []
#			temp2[index]["POSITION"] = []
#			temp2[index]["LOCATION"] = []
#			temp2[index]["AIR"].append({})
#			temp2[index]["POSITION"].append({})
#			temp2[index]["LOCATION"].append({})
#			acid = temp1[1]
#			cid = temp1[4]
#			for i in range(0, len(field)):
#				if i not in [2,5,6,7,8,9,10,11]:
#					temp2[index]["AIR"][0][field[i]] = temp1[i]
#				if i in [1]:
#					temp2[index]["AIR"][0]['ARL_COD'] = temp1[i][0:3]
#					temp2[index]["AIR"][0]['FLI_NUM'] = temp1[i][3::]
#				if i in [5]:
#					temp2[index]["AIR"][0]['ORIG_DATE'] = temp1[i][0:8]
#					temp2[index]["AIR"][0]['ORIG_TIME'] = temp1[i][9::]
#				if i in [6]:
#					temp2[index]["AIR"][0]['ARR_EST_DATE'] = temp1[i][0:8]
#					temp2[index]["AIR"][0]['ARR_EST_TIME'] = temp1[i][9::]
#				if i in [7]:
#					temp2[index]["AIR"][0]['POSIT_DATE'] = []
#					temp2[index]["AIR"][0]['POSIT_TIME'] = []
#					temp2[index]["AIR"][0]['POSIT_DATE'].append(temp1[i][0:8])
#					temp2[index]["AIR"][0]['POSIT_TIME'].append(temp1[i][9::])
#				if i in[8]:
#					temp2[index]["LOCATION"][0]['type'] = 'linestring'
#					temp2[index]["LOCATION"][0]['coordinates'] = []
#					temp2[index]["LOCATION"][0]['coordinates'].append([((float(temp1[i+1]))),(float(temp1[i]))])
#				if i in [9]:
#					temp3=[]
#				if i in [10,11]:
#					temp2[index]["POSITION"][0][field[i]] = []
#					temp2[index]["POSITION"][0][field[i]].append(float(temp1[i]))
#			n += 1
#		else:
#			index = uniqueList.index(temp1[0] +'_'+temp1[1] +'_'+temp1[2])
#			temp2[index]["LOCATION"][0]['coordinates'].append([((float(temp1[9]))),(float(temp1[8]))])
#			temp2[index]["POSITION"][0]['GROUNDSPEED'].append(float(temp1[10]))
#			temp2[index]["POSITION"][0]['ALTITUDE'].append(float(temp1[11]))
#			temp2[index]["AIR"][0]['POSIT_DATE'].append(temp1[7][0:8])
#			temp2[index]["AIR"][0]['POSIT_TIME'].append(temp1[7][9::])
#for i, item in enumerate(temp2):
#	item = str(item).replace('\'','\"')
#	#json = open(acList[i]+'_'+cidList[i]+'_'+str(i)+'.json', 'wb')
#	json = open(uniqueList[i]+'.json', 'wb')
#	json.write(item)
#	json.close()
