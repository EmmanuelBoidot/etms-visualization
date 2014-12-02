import json
import csv

fid = open('FLIGHT_PLAN_EN_CP_2014_part3.csv','rb')
#fid = open('test.csv','rb')
r, n = 0, 0
index=0
for row in fid:
	row = row.replace('\r\n', '')
	row = row.replace('"', '')
	if r == 0:
		field2 = row.split(',')
		r += 1
	else:
		temp1 = row.split(',')
		if temp1[0][3:5] in 'JAN':
			temp2 = {}		
			temp2["PLAN"]=[]
			temp2["PLAN"].append({})
			temp2["PLAN"][0]["LF"]=[]
			temp2["PLAN"][0]["LF"].append({})
			temp2["PLAN"][0]["LF"][0]["WAYPT_coord"] = []
			temp2["PLAN"][0]["LF"][0]["WAYPT_coord"].append({})
			temp2["PLAN"][0]["LF"][0]["FPWAYPT_coord"] = []
			temp2["PLAN"][0]["LF"][0]["FPWAYPT_coord"].append({})
			temp2["PLAN"][0]["PD"] = []
			temp2["PLAN"][0]["PD"].append({})
			temp2["PLAN"][0]["PD"][0]["WAYPT_coord"] = []
			temp2["PLAN"][0]["PD"][0]["WAYPT_coord"].append({})
			temp2["PLAN"][0]["PD"][0]["FPWAYPT_coord"] = []
			temp2["PLAN"][0]["PD"][0]["FPWAYPT_coord"].append({})
			temp2["PLAN"][0]["LA"] = []
			temp2["PLAN"][0]["LA"].append({})
			temp2["PLAN"][0]["LA"][0]["WAYPT_coord"] = []
			temp2["PLAN"][0]["LA"][0]["WAYPT_coord"].append({})
			temp2["PLAN"][0]["LA"][0]["FPWAYPT_coord"] = []
			temp2["PLAN"][0]["LA"][0]["FPWAYPT_coord"].append({})
			temp2["PLAN"][0]["AIR"]=[]
			temp2["PLAN"][0]["AIR"].append({})
			# ORIG 0-68
			date = temp1[0]
			acid = temp1[1]
			ARR_APRT = temp1[4]
			D40_coord = [-float(temp1[6])/60, float(temp1[5])/60]
			D40_alt = temp1[7]
			D40_time = temp1[8]
			D40_distflown = temp1[9]
			D40_dura = temp1[10]
			D40_bear_from_aprt = temp1[11]
			D40_GCD = temp1[12]
			D40_CF = temp1[13]
			D100_coord = [-float(temp1[15])/60, float(temp1[14])/60]
			D100_alt = temp1[16]
			D100_time = temp1[17]
			D100_distflown = temp1[18]
			D100_dura = temp1[19]
			D100_bear_from_aprt = temp1[20]
			D100_CGD = temp1[21]
			D100_CF = temp1[22]
			if temp1[24]!= '' and temp1[23] != '':
				A200_coord = [-float(temp1[24])/60, float(temp1[23])/60]
			else:
				A200_coord =''
			A200_alt = temp1[25]
			temp2["PLAN"][0]["AIR"][0]['ALTITUDE']=temp1[57]
			temp2["PLAN"][0]["AIR"][0]['A200_ALT']=A200_alt
			A200_time = temp1[26]
			A200_distflown = temp1[27]
			A200_dura = temp1[28]
			A200_bear_from_aprt = temp1[29]
			A200_CGD = temp1[30]
			A200_CF = temp1[31]
			A100_coord = [-float(temp1[33])/60,float(temp1[32])/60]
			A100_alt = temp1[34]
			temp2["PLAN"][0]["AIR"][0]['A100_ALT']=A100_alt
			A100_time = temp1[35]
			A100_distflown = temp1[36]
			A100_dura = temp1[37]
			A100_bear_from_aprt = temp1[38]
			A100_CGD = temp1[39]
			A100_CF = temp1[40]
			
			
			A40_coord = [-float(temp1[42])/60,float(temp1[41])/60]
			A40_alt = temp1[43]
			temp2["PLAN"][0]["AIR"][0]['A40_ALT']=A40_alt
			A40_time = temp1[44]
			A40_distflown = temp1[45]
			A40_dura = temp1[46]
			A40_bear_from_aprt = temp1[47]
			A40_CGD = temp1[48]
			A40_CF = temp1[49]
			##
			temp2["PLAN"][0]["AIR"][0]['ACT_DATE'] = temp1[0]
			temp2["PLAN"][0]["AIR"][0]['ARL_COD'] = acid[0:3]
			temp2["PLAN"][0]["AIR"][0]['FLI_NUM'] = acid[3::]
			temp2["PLAN"][0]["AIR"][0]['FLIGHT_INDEX'] = temp1[2]
			temp2["PLAN"][0]["AIR"][0]['DEP_APRT'] = temp1[3]
			temp2["PLAN"][0]["AIR"][0]['ARR_APRT'] = ARR_APRT
			temp2["PLAN"][0]["AIR"][0]['D40_coord'] = D40_coord
			temp2["PLAN"][0]["AIR"][0]['D40_ALT']=D40_alt
			temp2["PLAN"][0]["AIR"][0]['D40_distflown'] = D40_distflown
			temp2["PLAN"][0]["AIR"][0]['D40_dura'] = D40_dura
			temp2["PLAN"][0]["AIR"][0]['D40_bear_from_aprt'] = D40_bear_from_aprt
			temp2["PLAN"][0]["AIR"][0]['D40_GCD'] = D40_GCD
			temp2["PLAN"][0]["AIR"][0]['D40_CF'] = D40_CF
			temp2["PLAN"][0]["AIR"][0]['D100_coord'] = D100_coord
			temp2["PLAN"][0]["AIR"][0]['D100_ALT']=D100_alt
			temp2["PLAN"][0]["AIR"][0]['D100_distflown'] = D100_distflown
			temp2["PLAN"][0]["AIR"][0]['D100_dura'] = D100_dura
			temp2["PLAN"][0]["AIR"][0]['D100_bear_from_aprt'] = D100_bear_from_aprt
			temp2["PLAN"][0]["AIR"][0]['D100_CGD'] = D100_CGD
			temp2["PLAN"][0]["AIR"][0]['D100_CF'] = D100_CF
			temp2["PLAN"][0]["AIR"][0]['A200_coord'] = A200_coord
			temp2["PLAN"][0]["AIR"][0]['A200_distflown'] = A200_distflown 
			temp2["PLAN"][0]["AIR"][0]['A200_dura'] = A200_dura
			temp2["PLAN"][0]["AIR"][0]['A200_bear_from_aprt'] = A200_bear_from_aprt
			temp2["PLAN"][0]["AIR"][0]['A200_CGD'] = A200_CGD 
			temp2["PLAN"][0]["AIR"][0]['A200_CF'] = A200_CF 
			temp2["PLAN"][0]["AIR"][0]['A100_coord'] = A100_coord 
			temp2["PLAN"][0]["AIR"][0]['A100_distflown'] = A100_distflown 
			temp2["PLAN"][0]["AIR"][0]['A100_dura'] = A100_dura
			temp2["PLAN"][0]["AIR"][0]['A100_bear_from_aprt'] = A100_bear_from_aprt 
			temp2["PLAN"][0]["AIR"][0]['A100_CGD'] = A100_CGD
			temp2["PLAN"][0]["AIR"][0]['A100_CF'] = A100_CF 		
			temp2["PLAN"][0]["AIR"][0]['A40_coord'] = A40_coord
			temp2["PLAN"][0]["AIR"][0]['A40_distflown'] = A40_distflown
			temp2["PLAN"][0]["AIR"][0]['A40_dura'] = A40_dura 
			temp2["PLAN"][0]["AIR"][0]['A40_bear_from_aprt'] = A40_bear_from_aprt 
			temp2["PLAN"][0]["AIR"][0]['A40_CGD'] = A40_CGD
			temp2["PLAN"][0]["AIR"][0]['A40_CF'] = A40_CF 
			##
			temp2["PLAN"][0]["AIR"][0]['D40_TIME']=(D40_time)[9::]
			temp2["PLAN"][0]["AIR"][0]['D100_TIME']=(D100_time)[9::]
			temp2["PLAN"][0]["AIR"][0]['A200_TIME']=(A200_time)[9::]
			temp2["PLAN"][0]["AIR"][0]['A100_TIME']=(A100_time)[9::]
			temp2["PLAN"][0]["AIR"][0]['A40_TIME']=(A40_time)[9::]
			temp2["PLAN"][0]["AIR"][0]['D40_DATE']=(D40_time)[0:8]
			temp2["PLAN"][0]["AIR"][0]['D100_DATE']=(D100_time)[0:8]
			temp2["PLAN"][0]["AIR"][0]['A200_DATE']=(A200_time)[0:8]
			temp2["PLAN"][0]["AIR"][0]['A100_DATE']=(A100_time)[0:8]
			temp2["PLAN"][0]["AIR"][0]['A40_DATE']=(A40_time)[0:8]
			temp2["PLAN"][0]["AIR"][0]['ARR_TIME'] = temp1[50][9::]
			temp2["PLAN"][0]["AIR"][0]['ARR_DATE'] = temp1[50][0:8]
			temp2["PLAN"][0]["AIR"][0]['ARR_distflown'] = temp1[51]
			temp2["PLAN"][0]["AIR"][0]['ARR_dura'] = temp1[52]
			temp2["PLAN"][0]["AIR"][0]['ARR_GCD'] = temp1[53]
			temp2["PLAN"][0]["AIR"][0]['ARR_CF'] = temp1[54]
			
	#FP ---------------------------------------------------------------------------------------------------------------------------		
			#FP_DEPT_TIME = temp1[55]
			temp2["PLAN"][0]["AIR"][0]['FP_DEP_TIME'] = temp1[55][9::]
			temp2["PLAN"][0]["AIR"][0]['FP_DEP_DATE'] = temp1[55][0:8]
			#FP_ARR_TIME = temp1[56]
			temp2["PLAN"][0]["AIR"][0]['FP_ARR_TIME'] = temp1[56][9::]
			temp2["PLAN"][0]["AIR"][0]['FP_ARR_DATE'] = temp1[56][0:8]
			temp2["PLAN"][0]["AIR"][0]['SPEED'] = temp1[58]
			temp2["PLAN"][0]["AIR"][0]['ACFT_TYPE'] = temp1[59]
			temp2["PLAN"][0]["AIR"][0]['PHYSICAL_CLASS'] = temp1[60]
			temp2["PLAN"][0]["AIR"][0]['USER_CLASS'] = temp1[61]
			temp2["PLAN"][0]["AIR"][0]['SCHED_DEP_DATE'] = temp1[62][0:8]
			temp2["PLAN"][0]["AIR"][0]['SCHED_DEP_TIME'] = temp1[62][9::]
			temp2["PLAN"][0]["AIR"][0]['SCHED_ARR_DATE'] = temp1[63][0:8]
			temp2["PLAN"][0]["AIR"][0]['SCHED_ARR_TIME'] = temp1[63][9::]
			temp2["PLAN"][0]["AIR"][0]['ACTUAL_DEP_DATE'] = temp1[64][0:8]
			temp2["PLAN"][0]["AIR"][0]['ACTUAL_DEP_TIME'] = temp1[64][9::]
			temp2["PLAN"][0]["AIR"][0]['ACTUAL_ARR_DATE'] = temp1[65][0:8]
			temp2["PLAN"][0]["AIR"][0]['ACTUAL_ARR_TIME'] = temp1[65][9::]
			temp2["PLAN"][0]["AIR"][0]['PRE_DEP_AMENDS'] = temp1[66]
			temp2["PLAN"][0]["AIR"][0]['POST_DEP_AMEND'] = temp1[67]
			temp2["PLAN"][0]["AIR"][0]['MSG_ORIG_TIME'] = temp1[68]	
			
	# working on LF 69-98---------------------------------------------------------------------------------------------------------------------------		
			LF_ARR_APRT = temp1[70]
			if temp1[76] != '' and temp1[77] != '' and temp1[79] != '' and temp1[80] != '' and temp1[84] != '' and temp1[85] != '' and temp1[89] != '' and temp1[90] != '' and temp1[94] != '' and temp1[95] != '':
				LF_DEP_coord = [-float(temp1[77])/60, float(temp1[76])/60]
				LF_D40_coord = [-float(temp1[80])/60, float(temp1[79])/60]
				LF_A100_coord = [-float(temp1[85])/60,float(temp1[84])/60]
				LF_A40_coord = [-float(temp1[90])/60,float(temp1[89])/60]
				LF_ARR_coord = [-float(temp1[95])/60,float(temp1[94])/60]
			LF_WAYPT = temp1[71]
			if temp1[72]=='':
				LF_FPWAYPT = temp1[72]
			elif temp1[72]!='' and temp1[72][0]==' ':
				LF_FPWAYPT = temp1[72][1::]	
			else: 
				LF_FPWAYPT = temp1[72]

			LF_WAYPT_coord = LF_WAYPT.split(' ')
			temp2["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['type'] = 'linestring'
			temp2["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'] = []
			if LF_WAYPT!= '':
				for i in range(0, len(LF_WAYPT_coord)):
					temp2["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(LF_WAYPT_coord[i][5:9])/60)),(float(LF_WAYPT_coord[i][0:4])/60)])
			else:
				temp2["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'].append(LF_WAYPT_coord)
				
			LF_FPWAYPT_coord = LF_FPWAYPT.split(' ')
			temp2["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
			temp2["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'] = []
			a=LF_FPWAYPT_coord[0][5:9]
			b=LF_FPWAYPT_coord[0][0:4]
			if LF_FPWAYPT!= ' ':
				for i in range(1, len(LF_FPWAYPT_coord)):
					temp2["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(LF_FPWAYPT_coord[i][5:9])/60)),(float(LF_FPWAYPT_coord[i][0:4])/60)])
			else:
				temp2["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'].append(LF_FPWAYPT_coord)
			
			LF_FIELD10 = temp1[73]
			LF_DEPFIXID = temp1[74]
			LF_ARRFIXID = temp1[75]
			LF_DEP_ARR_GC = temp1[78]
			LF_D40_ACT_DIST = temp1[81]
			LF_D40_GC = temp1[82]
			LF_D40_DIR_DIST = temp1[83]
			LF_A100_ACT_DIST = temp1[86]
			LF_A100_GC = temp1[87]
			LF_A100_DIR_DIST = temp1[88]
			LF_A40_ACT_DIST	= temp1[91]
			LF_A40_GC = temp1[92]
			LF_A40_DIR_DIST = temp1[93]
			LF_ARR_ACT_DIST	= temp1[96]
			LF_ARR_GC = temp1[97]	
			LF_ARR_DIR_DIST = temp1[98]	
			temp2["PLAN"][0]["LF"][0]['ARR_APRT'] = LF_ARR_APRT
			temp2["PLAN"][0]["LF"][0]['DEP_coord']=LF_DEP_coord
			temp2["PLAN"][0]["LF"][0]['D40_coord']=LF_D40_coord
			temp2["PLAN"][0]["LF"][0]['A100_coord']=LF_A100_coord
			temp2["PLAN"][0]["LF"][0]['A40_coord']=LF_A40_coord
			temp2["PLAN"][0]["LF"][0]['ARR_coord']=LF_ARR_coord
			temp2["PLAN"][0]["LF"][0]['WAYPT']=LF_WAYPT
			temp2["PLAN"][0]["LF"][0]['FPWAYPT']=LF_FPWAYPT
			temp2["PLAN"][0]["LF"][0]['FIELD10']=LF_FIELD10
			temp2["PLAN"][0]["LF"][0]['DEPFIXID']=LF_DEPFIXID
			temp2["PLAN"][0]["LF"][0]['ARRFIXID']=LF_ARRFIXID 
			temp2["PLAN"][0]["LF"][0]['DEP_ARR_GC']=LF_DEP_ARR_GC
			temp2["PLAN"][0]["LF"][0]['D40_ACT_DIST']=LF_D40_ACT_DIST
			temp2["PLAN"][0]["LF"][0]['D40_GC']=LF_D40_GC
			temp2["PLAN"][0]["LF"][0]['D40_DIR_DIST']=LF_D40_DIR_DIST
			temp2["PLAN"][0]["LF"][0]['A100_ACT_DIST']=LF_A100_ACT_DIST
			temp2["PLAN"][0]["LF"][0]['A100_GC']=LF_A100_GC
			temp2["PLAN"][0]["LF"][0]['A100_DIR_DIST']=LF_A100_DIR_DIST
			temp2["PLAN"][0]["LF"][0]['A40_ACT_DIST']=LF_A40_ACT_DIST
			temp2["PLAN"][0]["LF"][0]['A40_GC']=LF_A40_GC
			temp2["PLAN"][0]["LF"][0]['A40_DIR_DIST']=LF_A40_DIR_DIST
			temp2["PLAN"][0]["LF"][0]['ARR_ACT_DIST']=LF_ARR_ACT_DIST
			temp2["PLAN"][0]["LF"][0]['ARR_GC']=LF_ARR_GC
			temp2["PLAN"][0]["LF"][0]['ARR_DIR_DIST']=LF_ARR_DIR_DIST
			
			
	# working on PD 99-128---------------------------------------------------------------------------------------------------------------------------		
			PD_ARR_APRT = temp1[100]
			if temp1[106] != '' and temp1[107] != '' and temp1[109] != '' and temp1[110] != '' and temp1[114] != '' and temp1[115] != '' and temp1[119] != '' and temp1[120] != '' and temp1[124] != '' and temp1[125] != '':
				PD_DEP_coord = [-float(temp1[107])/60, float(temp1[106])/60]
				PD_D40_coord = [-float(temp1[110])/60, float(temp1[109])/60]
				PD_A100_coord = [-float(temp1[115])/60,float(temp1[114])/60]
				PD_A40_coord = [-float(temp1[120])/60,float(temp1[119])/60]
				PD_ARR_coord = [-float(temp1[125])/60,float(temp1[124])/60]
			PD_WAYPT = temp1[101]
			if temp1[102]=='':
				PD_FPWAYPT = temp1[102]
			elif temp1[102]!='' and temp1[102][0]=='':
				PD_FPWAYPT = temp1[102][1::]	
			else: 
				PD_FPWAYPT = temp1[102]
			PD_FIELD10 = temp1[103]
			PD_DEPFIXID = temp1[104]
			PD_ARRFIXID = temp1[105]
			PD_DEP_ARR_GC = temp1[108]
			PD_D40_ACT_DIST = temp1[111]
			PD_D40_GC = temp1[112]
			PD_D40_DIR_DIST = temp1[113]
			PD_A100_ACT_DIST = temp1[116]
			PD_A100_GC = temp1[117]
			PD_A100_DIR_DIST = temp1[118]
			PD_A40_ACT_DIST = temp1[121]
			PD_A40_GC = temp1[122]
			PD_A40_DIR_DIST = temp1[123]
			PD_ARR_ACT_DIST =temp1[126]
			PD_ARR_GC = temp1[127]
			PD_ARR_DIR_DIST = temp1[128]
			
			PD_WAYPT_coord = PD_WAYPT.split(' ')
			temp2["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['type'] = 'linestring'
			temp2["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'] = []
			if PD_WAYPT!= '':
				for i in range(0, len(PD_WAYPT_coord)):
					temp2["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(PD_WAYPT_coord[i][5:9])/60)),(float(PD_WAYPT_coord[i][0:4])/60)])
			else:
				temp2["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'].append(PD_WAYPT_coord)
				
			PD_FPWAYPT_coord = PD_FPWAYPT.split(' ')
			temp2["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
			temp2["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'] = []
			if PD_FPWAYPT!= ' ':
				for i in range(1, len(PD_FPWAYPT_coord)):
					temp2["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(PD_FPWAYPT_coord[i][5:9])/60)),(float(PD_FPWAYPT_coord[i][0:4])/60)])
			else:
				temp2["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'].append(PD_FPWAYPT_coord)
			temp2["PLAN"][0]["PD"][0]['ARR_APRT'] = PD_ARR_APRT
			temp2["PLAN"][0]["PD"][0]['DEP_coord']=PD_DEP_coord
			temp2["PLAN"][0]["PD"][0]['D40_coord']=PD_D40_coord
			temp2["PLAN"][0]["PD"][0]['A100_coord']=PD_A100_coord
			temp2["PLAN"][0]["PD"][0]['A40_coord']=PD_A40_coord
			temp2["PLAN"][0]["PD"][0]['ARR_coord']=PD_ARR_coord
			temp2["PLAN"][0]["PD"][0]['WAYPT']=PD_WAYPT
			temp2["PLAN"][0]["PD"][0]['FPWAYPT']=PD_FPWAYPT
			temp2["PLAN"][0]["PD"][0]['FIELD10']=PD_FIELD10
			temp2["PLAN"][0]["PD"][0]['DEPFIXID']=PD_DEPFIXID
			temp2["PLAN"][0]["PD"][0]['ARRFIXID']=PD_ARRFIXID 
			temp2["PLAN"][0]["PD"][0]['DEP_ARR_GC']=PD_DEP_ARR_GC
			temp2["PLAN"][0]["PD"][0]['D40_ACT_DIST']=PD_D40_ACT_DIST
			temp2["PLAN"][0]["PD"][0]['D40_GC']=PD_D40_GC
			temp2["PLAN"][0]["PD"][0]['D40_DIR_DIST']=PD_D40_DIR_DIST
			temp2["PLAN"][0]["PD"][0]['A100_ACT_DIST']=PD_A100_ACT_DIST
			temp2["PLAN"][0]["PD"][0]['A100_GC']=PD_A100_GC
			temp2["PLAN"][0]["PD"][0]['A100_DIR_DIST']=PD_A100_DIR_DIST
			temp2["PLAN"][0]["PD"][0]['A40_ACT_DIST']=PD_A40_ACT_DIST
			temp2["PLAN"][0]["PD"][0]['A40_GC']=PD_A40_GC
			temp2["PLAN"][0]["PD"][0]['A40_DIR_DIST']=PD_A40_DIR_DIST
			temp2["PLAN"][0]["PD"][0]['ARR_ACT_DIST']=PD_ARR_ACT_DIST
			temp2["PLAN"][0]["PD"][0]['ARR_GC']=PD_ARR_GC
			temp2["PLAN"][0]["PD"][0]['ARR_DIR_DIST']=PD_ARR_DIR_DIST
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
			if temp1[132]=='':
				LA_FPWAYPT = temp1[132]
			elif temp1[132]!='' and temp1[132][0]==' ':
				LA_FPWAYPT = temp1[132][1::]
			else: 
				LA_FPWAYPT = temp1[132]
			LA_FIELD10 = temp1[133]
			LA_DEPFIXID = temp1[134]
			LA_ARRFIXID = temp1[135]
			LA_DEP_ARR_GC = temp1[138]
			LA_D40_ACT_DIST = temp1[141]
			LA_D40_GC = temp1[142]
			LA_D40_DIR_DIST = temp1[143]
			LA_A100_ACT_DIST = temp1[146]
			LA_A100_GC = temp1[147]
			LA_A100_DIR_DIST = temp1[148]
			LA_A40_ACT_DIST = temp1[151]
			LA_A40_GC = temp1[152]
			LA_A40_DIR_DIST = temp1[153]
			LA_ARR_ACT_DIST= temp1[156]	
			LA_ARR_GC = temp1[157]
			LA_ARR_DIR_DIST	= temp1[158]
			LA_WAYPT_coord = LA_WAYPT.split(' ')
			temp2["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['type'] = 'linestring'
			temp2["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'] = []
			if LA_WAYPT!= '':
				for i in range(0, len(LA_WAYPT_coord)):
					temp2["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(LA_WAYPT_coord[i][5:9])/60)),(float(LA_WAYPT_coord[i][0:4])/60)])
			else:
				temp2["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'].append(LA_WAYPT_coord)
				
			LA_FPWAYPT_coord = LA_FPWAYPT.split(' ')
			temp2["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
			temp2["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['coordinates'] = []
			if LA_FPWAYPT!= ' ':
				for i in range(1, len(LA_FPWAYPT_coord)):
					temp2["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(LA_FPWAYPT_coord[i][5:9])/60)),(float(LA_FPWAYPT_coord[i][0:4])/60)])
			else:
				temp2["FPWAYPT_coord"][0]['coordinates'].append(LA_FPWAYPT_coord)
			temp2["PLAN"][0]["LA"][0]['ARR_APRT'] = LA_ARR_APRT
			temp2["PLAN"][0]["LA"][0]['DEP_coord']=LA_DEP_coord
			temp2["PLAN"][0]["LA"][0]['D40_coord']=LA_D40_coord
			temp2["PLAN"][0]["LA"][0]['A100_coord']=LA_A100_coord
			temp2["PLAN"][0]["LA"][0]['A40_coord']=LA_A40_coord
			temp2["PLAN"][0]["LA"][0]['ARR_coord']=LA_ARR_coord
			temp2["PLAN"][0]["LA"][0]['WAYPT']=LA_WAYPT
			temp2["PLAN"][0]["LA"][0]['FPWAYPT']=LA_FPWAYPT
			temp2["PLAN"][0]["LA"][0]['FIELD10']=LA_FIELD10
			temp2["PLAN"][0]["LA"][0]['DEPFIXID']=LA_DEPFIXID
			temp2["PLAN"][0]["LA"][0]['ARRFIXID']=LA_ARRFIXID 
			temp2["PLAN"][0]["LA"][0]['DEP_ARR_GC']=LA_DEP_ARR_GC
			temp2["PLAN"][0]["LA"][0]['D40_ACT_DIST']=LA_D40_ACT_DIST
			temp2["PLAN"][0]["LA"][0]['D40_GC']=LA_D40_GC
			temp2["PLAN"][0]["LA"][0]['D40_DIR_DIST']=LA_D40_DIR_DIST
			temp2["PLAN"][0]["LA"][0]['A100_ACT_DIST']=LA_A100_ACT_DIST
			temp2["PLAN"][0]["LA"][0]['A100_GC']=LA_A100_GC
			temp2["PLAN"][0]["LA"][0]['A100_DIR_DIST']=LA_A100_DIR_DIST
			temp2["PLAN"][0]["LA"][0]['A40_ACT_DIST']=LA_A40_ACT_DIST
			temp2["PLAN"][0]["LA"][0]['A40_GC']=LA_A40_GC
			temp2["PLAN"][0]["LA"][0]['A40_DIR_DIST']=LA_A40_DIR_DIST
			temp2["PLAN"][0]["LA"][0]['ARR_ACT_DIST']=LA_ARR_ACT_DIST
			temp2["PLAN"][0]["LA"][0]['ARR_GC']=LA_ARR_GC
			temp2["PLAN"][0]["LA"][0]['ARR_DIR_DIST']=LA_ARR_DIR_DIST
	#extra
			D40_A40_ACT_DIST = temp1[159]
			D40_A40_GC_DIST	 = temp1[160]
			D40_A40_DIR_DIST  = temp1[161]
			D40_A40_ACH_DIST = temp1[162]
			D40_A100_ACT_DIST = temp1[163]
			D40_A100_GC_DIST= temp1[164]
			D40_A100_DIR_DIST  = temp1[165]
			D40_A100_ACH_DIST= temp1[166]
			DEP_CENTER  = temp1[167]
			DEP_CONUS= temp1[168]
			ARR_CENTER  = temp1[169]
			ARR_CONUS= temp1[170]
			DEP_RANK  = temp1[171]
			ARR_RANK= temp1[172]
			LF_DIVERSION = temp1[173]
			USER_CLASS = temp1[174]
			ACFT_EQUIP  = temp1[175]
			#FP_LF_FLAG  = temp1[176]
			TZ_QUAL_FLAG = temp1[177]
			temp2["PLAN"][0]["AIR"][0]['D40_A40_ACT_DIST'] = D40_A40_ACT_DIST
			temp2["PLAN"][0]["AIR"][0]['D40_A40_GC_DIST'] = D40_A40_GC_DIST
			temp2["PLAN"][0]["AIR"][0]['D40_A40_DIR_DIST'] = D40_A40_DIR_DIST
			temp2["PLAN"][0]["AIR"][0]['D40_A40_ACH_DIST'] = D40_A40_ACH_DIST
			temp2["PLAN"][0]["AIR"][0]['D40_A100_ACT_DIST'] = D40_A100_ACT_DIST
			temp2["PLAN"][0]["AIR"][0]['D40_A100_GC_DIST'] = D40_A100_GC_DIST
			temp2["PLAN"][0]["AIR"][0]['D40_A100_DIR_DIST'] = D40_A100_DIR_DIST
			temp2["PLAN"][0]["AIR"][0]['D40_A100_ACH_DIST'] = D40_A100_ACH_DIST
			temp2["PLAN"][0]["AIR"][0]['DEP_CENTER'] = DEP_CENTER
			temp2["PLAN"][0]["AIR"][0]['DEP_CONUS'] = DEP_CONUS
			temp2["PLAN"][0]["AIR"][0]['ARR_CENTER'] = ARR_CENTER
			temp2["PLAN"][0]["AIR"][0]['ARR_CONUS'] = ARR_CONUS
			temp2["PLAN"][0]["AIR"][0]['DEP_RANK'] = DEP_RANK
			temp2["PLAN"][0]["AIR"][0]['ARR_RANK'] = ARR_RANK
			temp2["PLAN"][0]["AIR"][0]['LF_DIVERSION'] = LF_DIVERSION
			temp2["PLAN"][0]["AIR"][0]['USER_CLASS'] = USER_CLASS
			temp2["PLAN"][0]["AIR"][0]['ACFT_EQUIP'] = ACFT_EQUIP
			#temp2["PLAN"][0]["AIR"][0] = FP_LF_FLAG
			temp2["PLAN"][0]["AIR"][0]['TZ_QUAL_FLAG'] = TZ_QUAL_FLAG
					###### end code
############### end plan
				
			print acid, date
			temp2 = str(temp2).replace('\'','\"')
			json = open(acid+'_'+date+'_'+temp1[2]+'.json', 'wb')
			json.write(temp2)
			json.close()
fid.close()