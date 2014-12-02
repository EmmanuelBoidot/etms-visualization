import json
import csv
from datetime import datetime


fid = open('TZ_CP_201301_02.csv','rb')
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
		if temp1[3][3:5] in 'JAN':
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
				fid2 = open('FLIGHT_PLAN_EN_CP_2013_part1.csv', 'rb')
				r2, n2 = 0, 0
				found_plan = 0
				for row2 in fid2:
					row2 = row2.replace('\r\n', '')
					row2 = row2.replace('"', '')
					if r == 0:
						field2 = row2.split(',')
						r += 1
					else:
						temp1_plan = row2.split(',')
						uniqueList_plan = temp1_plan[1] +'_'+temp1_plan[0] +'_'+temp1_plan[2]
					if uniqueList_plan == (temp1[2] +'_'+temp1[3] +'_'+temp1[4]):
						found_plan = 1
						###### insert code
						temp2[index]["PLAN"]=[]
						temp2[index]["PLAN"].append({})
						temp2[index]["PLAN"][0]["LF"]=[]
						temp2[index]["PLAN"][0]["LF"].append({})
						temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"] = []
						temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"].append({})
						temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"] = []
						temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"].append({})
						temp2[index]["PLAN"][0]["PD"] = []
						temp2[index]["PLAN"][0]["PD"].append({})
						temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"] = []
						temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"].append({})
						temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"] = []
						temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"].append({})
						temp2[index]["PLAN"][0]["LA"] = []
						temp2[index]["PLAN"][0]["LA"].append({})
						temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"] = []
						temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"].append({})
						temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"] = []
						temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"].append({})
						temp2[index]["PLAN"][0]["AIR"]=[]
						temp2[index]["PLAN"][0]["AIR"].append({})
						# ORIG 0-68
						date = temp1_plan[0]
						acid = temp1_plan[1]
						ARR_APRT = temp1_plan[4]
						D40_coord = [-float(temp1_plan[6])/60, float(temp1_plan[5])/60]
						D40_alt = temp1_plan[7]
						D40_time = temp1_plan[8]
						D40_distflown = temp1_plan[9]
						D40_dura = temp1_plan[10]
						D40_bear_from_aprt = temp1_plan[11]
						D40_GCD = temp1_plan[12]
						D40_CF = temp1_plan[13]
						D100_coord = [-float(temp1_plan[15])/60, float(temp1_plan[14])/60]
						D100_alt = temp1_plan[16]
						D100_time = temp1_plan[17]
						D100_distflown = temp1_plan[18]
						D100_dura = temp1_plan[19]
						D100_bear_from_aprt = temp1_plan[20]
						D100_CGD = temp1_plan[21]
						D100_CF = temp1_plan[22]
						if temp1_plan[24]!= '' and temp1_plan[23] != '':
							A200_coord = [-float(temp1_plan[24])/60, float(temp1_plan[23])/60]
						else:
							A200_coord =''
						A200_alt = temp1_plan[25]
						temp2[index]["PLAN"][0]["AIR"][0]['ALTITUDE']=temp1_plan[57]
						temp2[index]["PLAN"][0]["AIR"][0]['A200_ALT']=A200_alt
						A200_time = temp1_plan[26]
						A200_distflown = temp1_plan[27]
						A200_dura = temp1_plan[28]
						A200_bear_from_aprt = temp1_plan[29]
						A200_CGD = temp1_plan[30]
						A200_CF = temp1_plan[31]
						A100_coord = [-float(temp1_plan[33])/60,float(temp1_plan[32])/60]
						A100_alt = temp1_plan[34]
						temp2[index]["PLAN"][0]["AIR"][0]['A100_ALT']=A100_alt
						A100_time = temp1_plan[35]
						A100_distflown = temp1_plan[36]
						A100_dura = temp1_plan[37]
						A100_bear_from_aprt = temp1_plan[38]
						A100_CGD = temp1_plan[39]
						A100_CF = temp1_plan[40]
						
						
						A40_coord = [-float(temp1_plan[42])/60,float(temp1_plan[41])/60]
						A40_alt = temp1_plan[43]
						temp2[index]["PLAN"][0]["AIR"][0]['A40_ALT']=A40_alt
						A40_time = temp1_plan[44]
						A40_distflown = temp1_plan[45]
						A40_dura = temp1_plan[46]
						A40_bear_from_aprt = temp1_plan[47]
						A40_CGD = temp1_plan[48]
						A40_CF = temp1_plan[49]
						##
						temp2[index]["PLAN"][0]["AIR"][0]['ACT_DATE'] = temp1_plan[0]
						temp2[index]["PLAN"][0]["AIR"][0]['ARL_COD'] = acid[0:3]
						temp2[index]["PLAN"][0]["AIR"][0]['FLI_NUM'] = acid[3::]
						temp2[index]["PLAN"][0]["AIR"][0]['FLIGHT_INDEX'] = temp1_plan[2]
						temp2[index]["PLAN"][0]["AIR"][0]['DEP_APRT'] = temp1_plan[3]
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_APRT'] = ARR_APRT
						temp2[index]["PLAN"][0]["AIR"][0]['D40_coord'] = D40_coord
						temp2[index]["PLAN"][0]["AIR"][0]['D40_ALT']=D40_alt
						temp2[index]["PLAN"][0]["AIR"][0]['D40_distflown'] = D40_distflown
						temp2[index]["PLAN"][0]["AIR"][0]['D40_dura'] = D40_dura
						temp2[index]["PLAN"][0]["AIR"][0]['D40_bear_from_aprt'] = D40_bear_from_aprt
						temp2[index]["PLAN"][0]["AIR"][0]['D40_GCD'] = D40_GCD
						temp2[index]["PLAN"][0]["AIR"][0]['D40_CF'] = D40_CF
						temp2[index]["PLAN"][0]["AIR"][0]['D100_coord'] = D100_coord
						temp2[index]["PLAN"][0]["AIR"][0]['D100_ALT']=D100_alt
						temp2[index]["PLAN"][0]["AIR"][0]['D100_distflown'] = D100_distflown
						temp2[index]["PLAN"][0]["AIR"][0]['D100_dura'] = D100_dura
						temp2[index]["PLAN"][0]["AIR"][0]['D100_bear_from_aprt'] = D100_bear_from_aprt
						temp2[index]["PLAN"][0]["AIR"][0]['D100_CGD'] = D100_CGD
						temp2[index]["PLAN"][0]["AIR"][0]['D100_CF'] = D100_CF
						temp2[index]["PLAN"][0]["AIR"][0]['A200_coord'] = A200_coord
						temp2[index]["PLAN"][0]["AIR"][0]['A200_distflown'] = A200_distflown 
						temp2[index]["PLAN"][0]["AIR"][0]['A200_dura'] = A200_dura
						temp2[index]["PLAN"][0]["AIR"][0]['A200_bear_from_aprt'] = A200_bear_from_aprt
						temp2[index]["PLAN"][0]["AIR"][0]['A200_CGD'] = A200_CGD 
						temp2[index]["PLAN"][0]["AIR"][0]['A200_CF'] = A200_CF 
						temp2[index]["PLAN"][0]["AIR"][0]['A100_coord'] = A100_coord 
						temp2[index]["PLAN"][0]["AIR"][0]['A100_distflown'] = A100_distflown 
						temp2[index]["PLAN"][0]["AIR"][0]['A100_dura'] = A100_dura
						temp2[index]["PLAN"][0]["AIR"][0]['A100_bear_from_aprt'] = A100_bear_from_aprt 
						temp2[index]["PLAN"][0]["AIR"][0]['A100_CGD'] = A100_CGD
						temp2[index]["PLAN"][0]["AIR"][0]['A100_CF'] = A100_CF 		
						temp2[index]["PLAN"][0]["AIR"][0]['A40_coord'] = A40_coord
						temp2[index]["PLAN"][0]["AIR"][0]['A40_distflown'] = A40_distflown
						temp2[index]["PLAN"][0]["AIR"][0]['A40_dura'] = A40_dura 
						temp2[index]["PLAN"][0]["AIR"][0]['A40_bear_from_aprt'] = A40_bear_from_aprt 
						temp2[index]["PLAN"][0]["AIR"][0]['A40_CGD'] = A40_CGD
						temp2[index]["PLAN"][0]["AIR"][0]['A40_CF'] = A40_CF 
						##
						temp2[index]["PLAN"][0]["AIR"][0]['D40_TIME']=(D40_time)[9::]
						temp2[index]["PLAN"][0]["AIR"][0]['D100_TIME']=(D100_time)[9::]
						temp2[index]["PLAN"][0]["AIR"][0]['A200_TIME']=(A200_time)[9::]
						temp2[index]["PLAN"][0]["AIR"][0]['A100_TIME']=(A100_time)[9::]
						temp2[index]["PLAN"][0]["AIR"][0]['A40_TIME']=(A40_time)[9::]
						temp2[index]["PLAN"][0]["AIR"][0]['D40_DATE']=(D40_time)[0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['D100_DATE']=(D100_time)[0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['A200_DATE']=(A200_time)[0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['A100_DATE']=(A100_time)[0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['A40_DATE']=(A40_time)[0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_TIME'] = temp1_plan[50][9::]
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_DATE'] = temp1_plan[50][0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_distflown'] = temp1_plan[51]
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_dura'] = temp1_plan[52]
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_GCD'] = temp1_plan[53]
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_CF'] = temp1_plan[54]
						
				#FP ---------------------------------------------------------------------------------------------------------------------------		
						#FP_DEPT_TIME = temp1_plan[55]
						temp2[index]["PLAN"][0]["AIR"][0]['FP_DEP_TIME'] = temp1_plan[55][9::]
						temp2[index]["PLAN"][0]["AIR"][0]['FP_DEP_DATE'] = temp1_plan[55][0:8]
						#FP_ARR_TIME = temp1_plan[56]
						temp2[index]["PLAN"][0]["AIR"][0]['FP_ARR_TIME'] = temp1_plan[56][9::]
						temp2[index]["PLAN"][0]["AIR"][0]['FP_ARR_DATE'] = temp1_plan[56][0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['SPEED'] = temp1_plan[58]
						temp2[index]["PLAN"][0]["AIR"][0]['ACFT_TYPE'] = temp1_plan[59]
						temp2[index]["PLAN"][0]["AIR"][0]['PHYSICAL_CLASS'] = temp1_plan[60]
						temp2[index]["PLAN"][0]["AIR"][0]['USER_CLASS'] = temp1_plan[61]
						temp2[index]["PLAN"][0]["AIR"][0]['SCHED_DEP_DATE'] = temp1_plan[62][0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['SCHED_DEP_TIME'] = temp1_plan[62][9::]
						temp2[index]["PLAN"][0]["AIR"][0]['SCHED_ARR_DATE'] = temp1_plan[63][0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['SCHED_ARR_TIME'] = temp1_plan[63][9::]
						temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_DEP_DATE'] = temp1_plan[64][0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_DEP_TIME'] = temp1_plan[64][9::]
						temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_ARR_DATE'] = temp1_plan[65][0:8]
						temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_ARR_TIME'] = temp1_plan[65][9::]
						temp2[index]["PLAN"][0]["AIR"][0]['PRE_DEP_AMENDS'] = temp1_plan[66]
						temp2[index]["PLAN"][0]["AIR"][0]['POST_DEP_AMEND'] = temp1_plan[67]
						temp2[index]["PLAN"][0]["AIR"][0]['MSG_ORIG_TIME'] = temp1_plan[68]	
						
				# working on LF 69-98---------------------------------------------------------------------------------------------------------------------------		
						LF_ARR_APRT = temp1_plan[70]
						if temp1_plan[76] != '' and temp1_plan[77] != '' and temp1_plan[79] != '' and temp1_plan[80] != '' and temp1_plan[84] != '' and temp1_plan[85] != '' and temp1_plan[89] != '' and temp1_plan[90] != '' and temp1_plan[94] != '' and temp1_plan[95] != '':
							LF_DEP_coord = [-float(temp1_plan[77])/60, float(temp1_plan[76])/60]
							LF_D40_coord = [-float(temp1_plan[80])/60, float(temp1_plan[79])/60]
							LF_A100_coord = [-float(temp1_plan[85])/60,float(temp1_plan[84])/60]
							LF_A40_coord = [-float(temp1_plan[90])/60,float(temp1_plan[89])/60]
							LF_ARR_coord = [-float(temp1_plan[95])/60,float(temp1_plan[94])/60]
						LF_WAYPT = temp1_plan[71]
						if temp1_plan[72]=='':
							LF_FPWAYPT = temp1_plan[72]
						elif temp1_plan[72]!='' and temp1_plan[72][0]==' ':
							LF_FPWAYPT = temp1_plan[72][1::]	
						else: 
							LF_FPWAYPT = temp1_plan[72]

						LF_WAYPT_coord = LF_WAYPT.split(' ')
						temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['type'] = 'linestring'
						temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'] = []
						if LF_WAYPT!= '':
							for i in range(0, len(LF_WAYPT_coord)):
								temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(LF_WAYPT_coord[i][5:9])/60)),(float(LF_WAYPT_coord[i][0:4])/60)])
						else:
							temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'].append(LF_WAYPT_coord)
							
						LF_FPWAYPT_coord = LF_FPWAYPT.split(' ')
						temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
						temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'] = []
						a=LF_FPWAYPT_coord[0][5:9]
						b=LF_FPWAYPT_coord[0][0:4]
						if LF_FPWAYPT!= ' ':
							for i in range(1, len(LF_FPWAYPT_coord)):
								temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(LF_FPWAYPT_coord[i][5:9])/60)),(float(LF_FPWAYPT_coord[i][0:4])/60)])
						else:
							temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'].append(LF_FPWAYPT_coord)
						
						LF_FIELD10 = temp1_plan[73]
						LF_DEPFIXID = temp1_plan[74]
						LF_ARRFIXID = temp1_plan[75]
						LF_DEP_ARR_GC = temp1_plan[78]
						LF_D40_ACT_DIST = temp1_plan[81]
						LF_D40_GC = temp1_plan[82]
						LF_D40_DIR_DIST = temp1_plan[83]
						LF_A100_ACT_DIST = temp1_plan[86]
						LF_A100_GC = temp1_plan[87]
						LF_A100_DIR_DIST = temp1_plan[88]
						LF_A40_ACT_DIST	= temp1_plan[91]
						LF_A40_GC = temp1_plan[92]
						LF_A40_DIR_DIST = temp1_plan[93]
						LF_ARR_ACT_DIST	= temp1_plan[96]
						LF_ARR_GC = temp1_plan[97]	
						LF_ARR_DIR_DIST = temp1_plan[98]	
						temp2[index]["PLAN"][0]["LF"][0]['ARR_APRT'] = LF_ARR_APRT
						temp2[index]["PLAN"][0]["LF"][0]['DEP_coord']=LF_DEP_coord
						temp2[index]["PLAN"][0]["LF"][0]['D40_coord']=LF_D40_coord
						temp2[index]["PLAN"][0]["LF"][0]['A100_coord']=LF_A100_coord
						temp2[index]["PLAN"][0]["LF"][0]['A40_coord']=LF_A40_coord
						temp2[index]["PLAN"][0]["LF"][0]['ARR_coord']=LF_ARR_coord
						temp2[index]["PLAN"][0]["LF"][0]['WAYPT']=LF_WAYPT
						temp2[index]["PLAN"][0]["LF"][0]['FPWAYPT']=LF_FPWAYPT
						temp2[index]["PLAN"][0]["LF"][0]['FIELD10']=LF_FIELD10
						temp2[index]["PLAN"][0]["LF"][0]['DEPFIXID']=LF_DEPFIXID
						temp2[index]["PLAN"][0]["LF"][0]['ARRFIXID']=LF_ARRFIXID 
						temp2[index]["PLAN"][0]["LF"][0]['DEP_ARR_GC']=LF_DEP_ARR_GC
						temp2[index]["PLAN"][0]["LF"][0]['D40_ACT_DIST']=LF_D40_ACT_DIST
						temp2[index]["PLAN"][0]["LF"][0]['D40_GC']=LF_D40_GC
						temp2[index]["PLAN"][0]["LF"][0]['D40_DIR_DIST']=LF_D40_DIR_DIST
						temp2[index]["PLAN"][0]["LF"][0]['A100_ACT_DIST']=LF_A100_ACT_DIST
						temp2[index]["PLAN"][0]["LF"][0]['A100_GC']=LF_A100_GC
						temp2[index]["PLAN"][0]["LF"][0]['A100_DIR_DIST']=LF_A100_DIR_DIST
						temp2[index]["PLAN"][0]["LF"][0]['A40_ACT_DIST']=LF_A40_ACT_DIST
						temp2[index]["PLAN"][0]["LF"][0]['A40_GC']=LF_A40_GC
						temp2[index]["PLAN"][0]["LF"][0]['A40_DIR_DIST']=LF_A40_DIR_DIST
						temp2[index]["PLAN"][0]["LF"][0]['ARR_ACT_DIST']=LF_ARR_ACT_DIST
						temp2[index]["PLAN"][0]["LF"][0]['ARR_GC']=LF_ARR_GC
						temp2[index]["PLAN"][0]["LF"][0]['ARR_DIR_DIST']=LF_ARR_DIR_DIST
						
						
				# working on PD 99-128---------------------------------------------------------------------------------------------------------------------------		
						PD_ARR_APRT = temp1_plan[100]
						if temp1_plan[106] != '' and temp1_plan[107] != '' and temp1_plan[109] != '' and temp1_plan[110] != '' and temp1_plan[114] != '' and temp1_plan[115] != '' and temp1_plan[119] != '' and temp1_plan[120] != '' and temp1_plan[124] != '' and temp1_plan[125] != '':
							PD_DEP_coord = [-float(temp1_plan[107])/60, float(temp1_plan[106])/60]
							PD_D40_coord = [-float(temp1_plan[110])/60, float(temp1_plan[109])/60]
							PD_A100_coord = [-float(temp1_plan[115])/60,float(temp1_plan[114])/60]
							PD_A40_coord = [-float(temp1_plan[120])/60,float(temp1_plan[119])/60]
							PD_ARR_coord = [-float(temp1_plan[125])/60,float(temp1_plan[124])/60]
						PD_WAYPT = temp1_plan[101]
						if temp1_plan[102]=='':
							PD_FPWAYPT = temp1_plan[102]
						elif temp1_plan[102]!='' and temp1_plan[102][0]=='':
							PD_FPWAYPT = temp1_plan[102][1::]	
						else: 
							PD_FPWAYPT = temp1_plan[102]
						PD_FIELD10 = temp1_plan[103]
						PD_DEPFIXID = temp1_plan[104]
						PD_ARRFIXID = temp1_plan[105]
						PD_DEP_ARR_GC = temp1_plan[108]
						PD_D40_ACT_DIST = temp1_plan[111]
						PD_D40_GC = temp1_plan[112]
						PD_D40_DIR_DIST = temp1_plan[113]
						PD_A100_ACT_DIST = temp1_plan[116]
						PD_A100_GC = temp1_plan[117]
						PD_A100_DIR_DIST = temp1_plan[118]
						PD_A40_ACT_DIST = temp1_plan[121]
						PD_A40_GC = temp1_plan[122]
						PD_A40_DIR_DIST = temp1_plan[123]
						PD_ARR_ACT_DIST =temp1_plan[126]
						PD_ARR_GC = temp1_plan[127]
						PD_ARR_DIR_DIST = temp1_plan[128]
						
						PD_WAYPT_coord = PD_WAYPT.split(' ')
						temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['type'] = 'linestring'
						temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'] = []
						if PD_WAYPT!= '':
							for i in range(0, len(PD_WAYPT_coord)):
								temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(PD_WAYPT_coord[i][5:9])/60)),(float(PD_WAYPT_coord[i][0:4])/60)])
						else:
							temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'].append(PD_WAYPT_coord)
							
						PD_FPWAYPT_coord = PD_FPWAYPT.split(' ')
						temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
						temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'] = []
						if PD_FPWAYPT!= ' ':
							for i in range(1, len(PD_FPWAYPT_coord)):
								temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(PD_FPWAYPT_coord[i][5:9])/60)),(float(PD_FPWAYPT_coord[i][0:4])/60)])
						else:
							temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'].append(PD_FPWAYPT_coord)
						temp2[index]["PLAN"][0]["PD"][0]['ARR_APRT'] = PD_ARR_APRT
						temp2[index]["PLAN"][0]["PD"][0]['DEP_coord']=PD_DEP_coord
						temp2[index]["PLAN"][0]["PD"][0]['D40_coord']=PD_D40_coord
						temp2[index]["PLAN"][0]["PD"][0]['A100_coord']=PD_A100_coord
						temp2[index]["PLAN"][0]["PD"][0]['A40_coord']=PD_A40_coord
						temp2[index]["PLAN"][0]["PD"][0]['ARR_coord']=PD_ARR_coord
						temp2[index]["PLAN"][0]["PD"][0]['WAYPT']=PD_WAYPT
						temp2[index]["PLAN"][0]["PD"][0]['FPWAYPT']=PD_FPWAYPT
						temp2[index]["PLAN"][0]["PD"][0]['FIELD10']=PD_FIELD10
						temp2[index]["PLAN"][0]["PD"][0]['DEPFIXID']=PD_DEPFIXID
						temp2[index]["PLAN"][0]["PD"][0]['ARRFIXID']=PD_ARRFIXID 
						temp2[index]["PLAN"][0]["PD"][0]['DEP_ARR_GC']=PD_DEP_ARR_GC
						temp2[index]["PLAN"][0]["PD"][0]['D40_ACT_DIST']=PD_D40_ACT_DIST
						temp2[index]["PLAN"][0]["PD"][0]['D40_GC']=PD_D40_GC
						temp2[index]["PLAN"][0]["PD"][0]['D40_DIR_DIST']=PD_D40_DIR_DIST
						temp2[index]["PLAN"][0]["PD"][0]['A100_ACT_DIST']=PD_A100_ACT_DIST
						temp2[index]["PLAN"][0]["PD"][0]['A100_GC']=PD_A100_GC
						temp2[index]["PLAN"][0]["PD"][0]['A100_DIR_DIST']=PD_A100_DIR_DIST
						temp2[index]["PLAN"][0]["PD"][0]['A40_ACT_DIST']=PD_A40_ACT_DIST
						temp2[index]["PLAN"][0]["PD"][0]['A40_GC']=PD_A40_GC
						temp2[index]["PLAN"][0]["PD"][0]['A40_DIR_DIST']=PD_A40_DIR_DIST
						temp2[index]["PLAN"][0]["PD"][0]['ARR_ACT_DIST']=PD_ARR_ACT_DIST
						temp2[index]["PLAN"][0]["PD"][0]['ARR_GC']=PD_ARR_GC
						temp2[index]["PLAN"][0]["PD"][0]['ARR_DIR_DIST']=PD_ARR_DIR_DIST
				# working on LA 129-158
						#temp2["AIR"][0]['ARR_APRT'] = temp1_plan[130]	
						LA_ARR_APRT = temp1_plan[130]
						if temp1_plan[136] != '' and temp1_plan[137] != '' and temp1_plan[139] != '' and temp1_plan[140] != '' and temp1_plan[144] != '' and temp1_plan[145] != '' and temp1_plan[149] != '' and temp1_plan[150] != '' and temp1_plan[154] != '' and temp1_plan[155] != '':
							LA_DEP_coord = [-float(temp1_plan[137])/60, float(temp1_plan[136])/60]
							LA_D40_coord = [-float(temp1_plan[140])/60, float(temp1_plan[139])/60]
							LA_A100_coord = [-float(temp1_plan[145])/60,float(temp1_plan[144])/60]
							LA_A40_coord = [-float(temp1_plan[150])/60,float(temp1_plan[149])/60]		
							LA_ARR_coord = [-float(temp1_plan[155])/60,float(temp1_plan[154])/60]
						LA_WAYPT = temp1_plan[131]
						if temp1_plan[132]=='':
							LA_FPWAYPT = temp1_plan[132]
						elif temp1_plan[132]!='' and temp1_plan[132][0]==' ':
							LA_FPWAYPT = temp1_plan[132][1::]
						else: 
							LA_FPWAYPT = temp1_plan[132]
						LA_FIELD10 = temp1_plan[133]
						LA_DEPFIXID = temp1_plan[134]
						LA_ARRFIXID = temp1_plan[135]
						LA_DEP_ARR_GC = temp1_plan[138]
						LA_D40_ACT_DIST = temp1_plan[141]
						LA_D40_GC = temp1_plan[142]
						LA_D40_DIR_DIST = temp1_plan[143]
						LA_A100_ACT_DIST = temp1_plan[146]
						LA_A100_GC = temp1_plan[147]
						LA_A100_DIR_DIST = temp1_plan[148]
						LA_A40_ACT_DIST = temp1_plan[151]
						LA_A40_GC = temp1_plan[152]
						LA_A40_DIR_DIST = temp1_plan[153]
						LA_ARR_ACT_DIST= temp1_plan[156]	
						LA_ARR_GC = temp1_plan[157]
						LA_ARR_DIR_DIST	= temp1_plan[158]
						LA_WAYPT_coord = LA_WAYPT.split(' ')
						temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['type'] = 'linestring'
						temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'] = []
						if LA_WAYPT!= '':
							for i in range(0, len(LA_WAYPT_coord)):
								temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(LA_WAYPT_coord[i][5:9])/60)),(float(LA_WAYPT_coord[i][0:4])/60)])
						else:
							temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'].append(LA_WAYPT_coord)
							
						LA_FPWAYPT_coord = LA_FPWAYPT.split(' ')
						temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
						temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['coordinates'] = []
						if LA_FPWAYPT!= ' ':
							for i in range(1, len(LA_FPWAYPT_coord)):
								temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(LA_FPWAYPT_coord[i][5:9])/60)),(float(LA_FPWAYPT_coord[i][0:4])/60)])
						else:
							temp2["FPWAYPT_coord"][0]['coordinates'].append(LA_FPWAYPT_coord)
						temp2[index]["PLAN"][0]["LA"][0]['ARR_APRT'] = LA_ARR_APRT
						temp2[index]["PLAN"][0]["LA"][0]['DEP_coord']=LA_DEP_coord
						temp2[index]["PLAN"][0]["LA"][0]['D40_coord']=LA_D40_coord
						temp2[index]["PLAN"][0]["LA"][0]['A100_coord']=LA_A100_coord
						temp2[index]["PLAN"][0]["LA"][0]['A40_coord']=LA_A40_coord
						temp2[index]["PLAN"][0]["LA"][0]['ARR_coord']=LA_ARR_coord
						temp2[index]["PLAN"][0]["LA"][0]['WAYPT']=LA_WAYPT
						temp2[index]["PLAN"][0]["LA"][0]['FPWAYPT']=LA_FPWAYPT
						temp2[index]["PLAN"][0]["LA"][0]['FIELD10']=LA_FIELD10
						temp2[index]["PLAN"][0]["LA"][0]['DEPFIXID']=LA_DEPFIXID
						temp2[index]["PLAN"][0]["LA"][0]['ARRFIXID']=LA_ARRFIXID 
						temp2[index]["PLAN"][0]["LA"][0]['DEP_ARR_GC']=LA_DEP_ARR_GC
						temp2[index]["PLAN"][0]["LA"][0]['D40_ACT_DIST']=LA_D40_ACT_DIST
						temp2[index]["PLAN"][0]["LA"][0]['D40_GC']=LA_D40_GC
						temp2[index]["PLAN"][0]["LA"][0]['D40_DIR_DIST']=LA_D40_DIR_DIST
						temp2[index]["PLAN"][0]["LA"][0]['A100_ACT_DIST']=LA_A100_ACT_DIST
						temp2[index]["PLAN"][0]["LA"][0]['A100_GC']=LA_A100_GC
						temp2[index]["PLAN"][0]["LA"][0]['A100_DIR_DIST']=LA_A100_DIR_DIST
						temp2[index]["PLAN"][0]["LA"][0]['A40_ACT_DIST']=LA_A40_ACT_DIST
						temp2[index]["PLAN"][0]["LA"][0]['A40_GC']=LA_A40_GC
						temp2[index]["PLAN"][0]["LA"][0]['A40_DIR_DIST']=LA_A40_DIR_DIST
						temp2[index]["PLAN"][0]["LA"][0]['ARR_ACT_DIST']=LA_ARR_ACT_DIST
						temp2[index]["PLAN"][0]["LA"][0]['ARR_GC']=LA_ARR_GC
						temp2[index]["PLAN"][0]["LA"][0]['ARR_DIR_DIST']=LA_ARR_DIR_DIST
				#extra
						D40_A40_ACT_DIST = temp1_plan[159]
						D40_A40_GC_DIST	 = temp1_plan[160]
						D40_A40_DIR_DIST  = temp1_plan[161]
						D40_A40_ACH_DIST = temp1_plan[162]
						D40_A100_ACT_DIST = temp1_plan[163]
						D40_A100_GC_DIST= temp1_plan[164]
						D40_A100_DIR_DIST  = temp1_plan[165]
						D40_A100_ACH_DIST= temp1_plan[166]
						DEP_CENTER  = temp1_plan[167]
						DEP_CONUS= temp1_plan[168]
						ARR_CENTER  = temp1_plan[169]
						ARR_CONUS= temp1_plan[170]
						DEP_RANK  = temp1_plan[171]
						ARR_RANK= temp1_plan[172]
						LF_DIVERSION = temp1_plan[173]
						USER_CLASS = temp1_plan[174]
						ACFT_EQUIP  = temp1_plan[175]
						#FP_LF_FLAG  = temp1_plan[176]
						TZ_QUAL_FLAG = temp1_plan[177]
						temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_ACT_DIST'] = D40_A40_ACT_DIST
						temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_GC_DIST'] = D40_A40_GC_DIST
						temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_DIR_DIST'] = D40_A40_DIR_DIST
						temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_ACH_DIST'] = D40_A40_ACH_DIST
						temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_ACT_DIST'] = D40_A100_ACT_DIST
						temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_GC_DIST'] = D40_A100_GC_DIST
						temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_DIR_DIST'] = D40_A100_DIR_DIST
						temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_ACH_DIST'] = D40_A100_ACH_DIST
						temp2[index]["PLAN"][0]["AIR"][0]['DEP_CENTER'] = DEP_CENTER
						temp2[index]["PLAN"][0]["AIR"][0]['DEP_CONUS'] = DEP_CONUS
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_CENTER'] = ARR_CENTER
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_CONUS'] = ARR_CONUS
						temp2[index]["PLAN"][0]["AIR"][0]['DEP_RANK'] = DEP_RANK
						temp2[index]["PLAN"][0]["AIR"][0]['ARR_RANK'] = ARR_RANK
						temp2[index]["PLAN"][0]["AIR"][0]['LF_DIVERSION'] = LF_DIVERSION
						temp2[index]["PLAN"][0]["AIR"][0]['USER_CLASS'] = USER_CLASS
						temp2[index]["PLAN"][0]["AIR"][0]['ACFT_EQUIP'] = ACFT_EQUIP
						#temp2[index]["PLAN"][0]["AIR"][0] = FP_LF_FLAG
						temp2[index]["PLAN"][0]["AIR"][0]['TZ_QUAL_FLAG'] = TZ_QUAL_FLAG
						###### end code
						fid2.close()
						break
					else:
						found_plan = 0
				if found_plan == 0:
					fid3 = open('FLIGHT_PLAN_EN_CP_2013_part2.csv', 'rb')
					r3, n3 = 0, 0
					found_plan = 0
					for row3 in fid3:
						row3 = row3.replace('\r\n', '')
						row3 = row3.replace('"', '')
						if r == 0:
							field3 = row3.split(',')
							r += 1
						else:
							temp1_plan = row3.split(',')
							uniqueList_plan = temp1_plan[1] +'_'+temp1_plan[0] +'_'+temp1_plan[2]
						if uniqueList_plan == (temp1[2] +'_'+temp1[3] +'_'+temp1[4]):
							found_plan = 1
							######insert code
							temp2[index]["PLAN"]=[]
							temp2[index]["PLAN"].append({})
							temp2[index]["PLAN"][0]["LF"]=[]
							temp2[index]["PLAN"][0]["LF"].append({})
							temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"] = []
							temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"].append({})
							temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"] = []
							temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"].append({})
							temp2[index]["PLAN"][0]["PD"] = []
							temp2[index]["PLAN"][0]["PD"].append({})
							temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"] = []
							temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"].append({})
							temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"] = []
							temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"].append({})
							temp2[index]["PLAN"][0]["LA"] = []
							temp2[index]["PLAN"][0]["LA"].append({})
							temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"] = []
							temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"].append({})
							temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"] = []
							temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"].append({})
							temp2[index]["PLAN"][0]["AIR"]=[]
							temp2[index]["PLAN"][0]["AIR"].append({})
							# ORIG 0-68
							date = temp1_plan[0]
							acid = temp1_plan[1]
							ARR_APRT = temp1_plan[4]
							D40_coord = [-float(temp1_plan[6])/60, float(temp1_plan[5])/60]
							D40_alt = temp1_plan[7]
							D40_time = temp1_plan[8]
							D40_distflown = temp1_plan[9]
							D40_dura = temp1_plan[10]
							D40_bear_from_aprt = temp1_plan[11]
							D40_GCD = temp1_plan[12]
							D40_CF = temp1_plan[13]
							D100_coord = [-float(temp1_plan[15])/60, float(temp1_plan[14])/60]
							D100_alt = temp1_plan[16]
							D100_time = temp1_plan[17]
							D100_distflown = temp1_plan[18]
							D100_dura = temp1_plan[19]
							D100_bear_from_aprt = temp1_plan[20]
							D100_CGD = temp1_plan[21]
							D100_CF = temp1_plan[22]
							if temp1_plan[24]!= '' and temp1_plan[23] != '':
								A200_coord = [-float(temp1_plan[24])/60, float(temp1_plan[23])/60]
							else:
								A200_coord =''
							A200_alt = temp1_plan[25]
							temp2[index]["PLAN"][0]["AIR"][0]['ALTITUDE']=temp1_plan[57]
							temp2[index]["PLAN"][0]["AIR"][0]['A200_ALT']=A200_alt
							A200_time = temp1_plan[26]
							A200_distflown = temp1_plan[27]
							A200_dura = temp1_plan[28]
							A200_bear_from_aprt = temp1_plan[29]
							A200_CGD = temp1_plan[30]
							A200_CF = temp1_plan[31]
							A100_coord = [-float(temp1_plan[33])/60,float(temp1_plan[32])/60]
							A100_alt = temp1_plan[34]
							temp2[index]["PLAN"][0]["AIR"][0]['A100_ALT']=A100_alt
							A100_time = temp1_plan[35]
							A100_distflown = temp1_plan[36]
							A100_dura = temp1_plan[37]
							A100_bear_from_aprt = temp1_plan[38]
							A100_CGD = temp1_plan[39]
							A100_CF = temp1_plan[40]
							
							
							A40_coord = [-float(temp1_plan[42])/60,float(temp1_plan[41])/60]
							A40_alt = temp1_plan[43]
							temp2[index]["PLAN"][0]["AIR"][0]['A40_ALT']=A40_alt
							A40_time = temp1_plan[44]
							A40_distflown = temp1_plan[45]
							A40_dura = temp1_plan[46]
							A40_bear_from_aprt = temp1_plan[47]
							A40_CGD = temp1_plan[48]
							A40_CF = temp1_plan[49]
							##
							temp2[index]["PLAN"][0]["AIR"][0]['ACT_DATE'] = temp1_plan[0]
							temp2[index]["PLAN"][0]["AIR"][0]['ARL_COD'] = acid[0:3]
							temp2[index]["PLAN"][0]["AIR"][0]['FLI_NUM'] = acid[3::]
							temp2[index]["PLAN"][0]["AIR"][0]['FLIGHT_INDEX'] = temp1_plan[2]
							temp2[index]["PLAN"][0]["AIR"][0]['DEP_APRT'] = temp1_plan[3]
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_APRT'] = ARR_APRT
							temp2[index]["PLAN"][0]["AIR"][0]['D40_coord'] = D40_coord
							temp2[index]["PLAN"][0]["AIR"][0]['D40_ALT']=D40_alt
							temp2[index]["PLAN"][0]["AIR"][0]['D40_distflown'] = D40_distflown
							temp2[index]["PLAN"][0]["AIR"][0]['D40_dura'] = D40_dura
							temp2[index]["PLAN"][0]["AIR"][0]['D40_bear_from_aprt'] = D40_bear_from_aprt
							temp2[index]["PLAN"][0]["AIR"][0]['D40_GCD'] = D40_GCD
							temp2[index]["PLAN"][0]["AIR"][0]['D40_CF'] = D40_CF
							temp2[index]["PLAN"][0]["AIR"][0]['D100_coord'] = D100_coord
							temp2[index]["PLAN"][0]["AIR"][0]['D100_ALT']=D100_alt
							temp2[index]["PLAN"][0]["AIR"][0]['D100_distflown'] = D100_distflown
							temp2[index]["PLAN"][0]["AIR"][0]['D100_dura'] = D100_dura
							temp2[index]["PLAN"][0]["AIR"][0]['D100_bear_from_aprt'] = D100_bear_from_aprt
							temp2[index]["PLAN"][0]["AIR"][0]['D100_CGD'] = D100_CGD
							temp2[index]["PLAN"][0]["AIR"][0]['D100_CF'] = D100_CF
							temp2[index]["PLAN"][0]["AIR"][0]['A200_coord'] = A200_coord
							temp2[index]["PLAN"][0]["AIR"][0]['A200_distflown'] = A200_distflown 
							temp2[index]["PLAN"][0]["AIR"][0]['A200_dura'] = A200_dura
							temp2[index]["PLAN"][0]["AIR"][0]['A200_bear_from_aprt'] = A200_bear_from_aprt
							temp2[index]["PLAN"][0]["AIR"][0]['A200_CGD'] = A200_CGD 
							temp2[index]["PLAN"][0]["AIR"][0]['A200_CF'] = A200_CF 
							temp2[index]["PLAN"][0]["AIR"][0]['A100_coord'] = A100_coord 
							temp2[index]["PLAN"][0]["AIR"][0]['A100_distflown'] = A100_distflown 
							temp2[index]["PLAN"][0]["AIR"][0]['A100_dura'] = A100_dura
							temp2[index]["PLAN"][0]["AIR"][0]['A100_bear_from_aprt'] = A100_bear_from_aprt 
							temp2[index]["PLAN"][0]["AIR"][0]['A100_CGD'] = A100_CGD
							temp2[index]["PLAN"][0]["AIR"][0]['A100_CF'] = A100_CF 		
							temp2[index]["PLAN"][0]["AIR"][0]['A40_coord'] = A40_coord
							temp2[index]["PLAN"][0]["AIR"][0]['A40_distflown'] = A40_distflown
							temp2[index]["PLAN"][0]["AIR"][0]['A40_dura'] = A40_dura 
							temp2[index]["PLAN"][0]["AIR"][0]['A40_bear_from_aprt'] = A40_bear_from_aprt 
							temp2[index]["PLAN"][0]["AIR"][0]['A40_CGD'] = A40_CGD
							temp2[index]["PLAN"][0]["AIR"][0]['A40_CF'] = A40_CF 
							##
							temp2[index]["PLAN"][0]["AIR"][0]['D40_TIME']=(D40_time)[9::]
							temp2[index]["PLAN"][0]["AIR"][0]['D100_TIME']=(D100_time)[9::]
							temp2[index]["PLAN"][0]["AIR"][0]['A200_TIME']=(A200_time)[9::]
							temp2[index]["PLAN"][0]["AIR"][0]['A100_TIME']=(A100_time)[9::]
							temp2[index]["PLAN"][0]["AIR"][0]['A40_TIME']=(A40_time)[9::]
							temp2[index]["PLAN"][0]["AIR"][0]['D40_DATE']=(D40_time)[0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['D100_DATE']=(D100_time)[0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['A200_DATE']=(A200_time)[0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['A100_DATE']=(A100_time)[0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['A40_DATE']=(A40_time)[0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_TIME'] = temp1_plan[50][9::]
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_DATE'] = temp1_plan[50][0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_distflown'] = temp1_plan[51]
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_dura'] = temp1_plan[52]
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_GCD'] = temp1_plan[53]
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_CF'] = temp1_plan[54]
							
					#FP ---------------------------------------------------------------------------------------------------------------------------		
							#FP_DEPT_TIME = temp1_plan[55]
							temp2[index]["PLAN"][0]["AIR"][0]['FP_DEP_TIME'] = temp1_plan[55][9::]
							temp2[index]["PLAN"][0]["AIR"][0]['FP_DEP_DATE'] = temp1_plan[55][0:8]
							#FP_ARR_TIME = temp1_plan[56]
							temp2[index]["PLAN"][0]["AIR"][0]['FP_ARR_TIME'] = temp1_plan[56][9::]
							temp2[index]["PLAN"][0]["AIR"][0]['FP_ARR_DATE'] = temp1_plan[56][0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['SPEED'] = temp1_plan[58]
							temp2[index]["PLAN"][0]["AIR"][0]['ACFT_TYPE'] = temp1_plan[59]
							temp2[index]["PLAN"][0]["AIR"][0]['PHYSICAL_CLASS'] = temp1_plan[60]
							temp2[index]["PLAN"][0]["AIR"][0]['USER_CLASS'] = temp1_plan[61]
							temp2[index]["PLAN"][0]["AIR"][0]['SCHED_DEP_DATE'] = temp1_plan[62][0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['SCHED_DEP_TIME'] = temp1_plan[62][9::]
							temp2[index]["PLAN"][0]["AIR"][0]['SCHED_ARR_DATE'] = temp1_plan[63][0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['SCHED_ARR_TIME'] = temp1_plan[63][9::]
							temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_DEP_DATE'] = temp1_plan[64][0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_DEP_TIME'] = temp1_plan[64][9::]
							temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_ARR_DATE'] = temp1_plan[65][0:8]
							temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_ARR_TIME'] = temp1_plan[65][9::]
							temp2[index]["PLAN"][0]["AIR"][0]['PRE_DEP_AMENDS'] = temp1_plan[66]
							temp2[index]["PLAN"][0]["AIR"][0]['POST_DEP_AMEND'] = temp1_plan[67]
							temp2[index]["PLAN"][0]["AIR"][0]['MSG_ORIG_TIME'] = temp1_plan[68]	
							
					# working on LF 69-98---------------------------------------------------------------------------------------------------------------------------		
							LF_ARR_APRT = temp1_plan[70]
							if temp1_plan[76] != '' and temp1_plan[77] != '' and temp1_plan[79] != '' and temp1_plan[80] != '' and temp1_plan[84] != '' and temp1_plan[85] != '' and temp1_plan[89] != '' and temp1_plan[90] != '' and temp1_plan[94] != '' and temp1_plan[95] != '':
								LF_DEP_coord = [-float(temp1_plan[77])/60, float(temp1_plan[76])/60]
								LF_D40_coord = [-float(temp1_plan[80])/60, float(temp1_plan[79])/60]
								LF_A100_coord = [-float(temp1_plan[85])/60,float(temp1_plan[84])/60]
								LF_A40_coord = [-float(temp1_plan[90])/60,float(temp1_plan[89])/60]
								LF_ARR_coord = [-float(temp1_plan[95])/60,float(temp1_plan[94])/60]
							LF_WAYPT = temp1_plan[71]
							if temp1_plan[72]=='':
								LF_FPWAYPT = temp1_plan[72]
							elif temp1_plan[72]!='' and temp1_plan[72][0]==' ':
								LF_FPWAYPT = temp1_plan[72][1::]	
							else: 
								LF_FPWAYPT = temp1_plan[72]

							LF_WAYPT_coord = LF_WAYPT.split(' ')
							temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['type'] = 'linestring'
							temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'] = []
							if LF_WAYPT!= '':
								for i in range(0, len(LF_WAYPT_coord)):
									temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(LF_WAYPT_coord[i][5:9])/60)),(float(LF_WAYPT_coord[i][0:4])/60)])
							else:
								temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'].append(LF_WAYPT_coord)
								
							LF_FPWAYPT_coord = LF_FPWAYPT.split(' ')
							temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
							temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'] = []
							a=LF_FPWAYPT_coord[0][5:9]
							b=LF_FPWAYPT_coord[0][0:4]
							if LF_FPWAYPT!= ' ':
								for i in range(1, len(LF_FPWAYPT_coord)):
									temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(LF_FPWAYPT_coord[i][5:9])/60)),(float(LF_FPWAYPT_coord[i][0:4])/60)])
							else:
								temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'].append(LF_FPWAYPT_coord)
							
							LF_FIELD10 = temp1_plan[73]
							LF_DEPFIXID = temp1_plan[74]
							LF_ARRFIXID = temp1_plan[75]
							LF_DEP_ARR_GC = temp1_plan[78]
							LF_D40_ACT_DIST = temp1_plan[81]
							LF_D40_GC = temp1_plan[82]
							LF_D40_DIR_DIST = temp1_plan[83]
							LF_A100_ACT_DIST = temp1_plan[86]
							LF_A100_GC = temp1_plan[87]
							LF_A100_DIR_DIST = temp1_plan[88]
							LF_A40_ACT_DIST	= temp1_plan[91]
							LF_A40_GC = temp1_plan[92]
							LF_A40_DIR_DIST = temp1_plan[93]
							LF_ARR_ACT_DIST	= temp1_plan[96]
							LF_ARR_GC = temp1_plan[97]	
							LF_ARR_DIR_DIST = temp1_plan[98]	
							temp2[index]["PLAN"][0]["LF"][0]['ARR_APRT'] = LF_ARR_APRT
							temp2[index]["PLAN"][0]["LF"][0]['DEP_coord']=LF_DEP_coord
							temp2[index]["PLAN"][0]["LF"][0]['D40_coord']=LF_D40_coord
							temp2[index]["PLAN"][0]["LF"][0]['A100_coord']=LF_A100_coord
							temp2[index]["PLAN"][0]["LF"][0]['A40_coord']=LF_A40_coord
							temp2[index]["PLAN"][0]["LF"][0]['ARR_coord']=LF_ARR_coord
							temp2[index]["PLAN"][0]["LF"][0]['WAYPT']=LF_WAYPT
							temp2[index]["PLAN"][0]["LF"][0]['FPWAYPT']=LF_FPWAYPT
							temp2[index]["PLAN"][0]["LF"][0]['FIELD10']=LF_FIELD10
							temp2[index]["PLAN"][0]["LF"][0]['DEPFIXID']=LF_DEPFIXID
							temp2[index]["PLAN"][0]["LF"][0]['ARRFIXID']=LF_ARRFIXID 
							temp2[index]["PLAN"][0]["LF"][0]['DEP_ARR_GC']=LF_DEP_ARR_GC
							temp2[index]["PLAN"][0]["LF"][0]['D40_ACT_DIST']=LF_D40_ACT_DIST
							temp2[index]["PLAN"][0]["LF"][0]['D40_GC']=LF_D40_GC
							temp2[index]["PLAN"][0]["LF"][0]['D40_DIR_DIST']=LF_D40_DIR_DIST
							temp2[index]["PLAN"][0]["LF"][0]['A100_ACT_DIST']=LF_A100_ACT_DIST
							temp2[index]["PLAN"][0]["LF"][0]['A100_GC']=LF_A100_GC
							temp2[index]["PLAN"][0]["LF"][0]['A100_DIR_DIST']=LF_A100_DIR_DIST
							temp2[index]["PLAN"][0]["LF"][0]['A40_ACT_DIST']=LF_A40_ACT_DIST
							temp2[index]["PLAN"][0]["LF"][0]['A40_GC']=LF_A40_GC
							temp2[index]["PLAN"][0]["LF"][0]['A40_DIR_DIST']=LF_A40_DIR_DIST
							temp2[index]["PLAN"][0]["LF"][0]['ARR_ACT_DIST']=LF_ARR_ACT_DIST
							temp2[index]["PLAN"][0]["LF"][0]['ARR_GC']=LF_ARR_GC
							temp2[index]["PLAN"][0]["LF"][0]['ARR_DIR_DIST']=LF_ARR_DIR_DIST
							
							
					# working on PD 99-128---------------------------------------------------------------------------------------------------------------------------		
							PD_ARR_APRT = temp1_plan[100]
							if temp1_plan[106] != '' and temp1_plan[107] != '' and temp1_plan[109] != '' and temp1_plan[110] != '' and temp1_plan[114] != '' and temp1_plan[115] != '' and temp1_plan[119] != '' and temp1_plan[120] != '' and temp1_plan[124] != '' and temp1_plan[125] != '':
								PD_DEP_coord = [-float(temp1_plan[107])/60, float(temp1_plan[106])/60]
								PD_D40_coord = [-float(temp1_plan[110])/60, float(temp1_plan[109])/60]
								PD_A100_coord = [-float(temp1_plan[115])/60,float(temp1_plan[114])/60]
								PD_A40_coord = [-float(temp1_plan[120])/60,float(temp1_plan[119])/60]
								PD_ARR_coord = [-float(temp1_plan[125])/60,float(temp1_plan[124])/60]
							PD_WAYPT = temp1_plan[101]
							if temp1_plan[102]=='':
								PD_FPWAYPT = temp1_plan[102]
							elif temp1_plan[102]!='' and temp1_plan[102][0]=='':
								PD_FPWAYPT = temp1_plan[102][1::]	
							else: 
								PD_FPWAYPT = temp1_plan[102]
							PD_FIELD10 = temp1_plan[103]
							PD_DEPFIXID = temp1_plan[104]
							PD_ARRFIXID = temp1_plan[105]
							PD_DEP_ARR_GC = temp1_plan[108]
							PD_D40_ACT_DIST = temp1_plan[111]
							PD_D40_GC = temp1_plan[112]
							PD_D40_DIR_DIST = temp1_plan[113]
							PD_A100_ACT_DIST = temp1_plan[116]
							PD_A100_GC = temp1_plan[117]
							PD_A100_DIR_DIST = temp1_plan[118]
							PD_A40_ACT_DIST = temp1_plan[121]
							PD_A40_GC = temp1_plan[122]
							PD_A40_DIR_DIST = temp1_plan[123]
							PD_ARR_ACT_DIST =temp1_plan[126]
							PD_ARR_GC = temp1_plan[127]
							PD_ARR_DIR_DIST = temp1_plan[128]
							
							PD_WAYPT_coord = PD_WAYPT.split(' ')
							temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['type'] = 'linestring'
							temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'] = []
							if PD_WAYPT!= '':
								for i in range(0, len(PD_WAYPT_coord)):
									temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(PD_WAYPT_coord[i][5:9])/60)),(float(PD_WAYPT_coord[i][0:4])/60)])
							else:
								temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'].append(PD_WAYPT_coord)
								
							PD_FPWAYPT_coord = PD_FPWAYPT.split(' ')
							temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
							temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'] = []
							if PD_FPWAYPT!= ' ':
								for i in range(1, len(PD_FPWAYPT_coord)):
									temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(PD_FPWAYPT_coord[i][5:9])/60)),(float(PD_FPWAYPT_coord[i][0:4])/60)])
							else:
								temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'].append(PD_FPWAYPT_coord)
							temp2[index]["PLAN"][0]["PD"][0]['ARR_APRT'] = PD_ARR_APRT
							temp2[index]["PLAN"][0]["PD"][0]['DEP_coord']=PD_DEP_coord
							temp2[index]["PLAN"][0]["PD"][0]['D40_coord']=PD_D40_coord
							temp2[index]["PLAN"][0]["PD"][0]['A100_coord']=PD_A100_coord
							temp2[index]["PLAN"][0]["PD"][0]['A40_coord']=PD_A40_coord
							temp2[index]["PLAN"][0]["PD"][0]['ARR_coord']=PD_ARR_coord
							temp2[index]["PLAN"][0]["PD"][0]['WAYPT']=PD_WAYPT
							temp2[index]["PLAN"][0]["PD"][0]['FPWAYPT']=PD_FPWAYPT
							temp2[index]["PLAN"][0]["PD"][0]['FIELD10']=PD_FIELD10
							temp2[index]["PLAN"][0]["PD"][0]['DEPFIXID']=PD_DEPFIXID
							temp2[index]["PLAN"][0]["PD"][0]['ARRFIXID']=PD_ARRFIXID 
							temp2[index]["PLAN"][0]["PD"][0]['DEP_ARR_GC']=PD_DEP_ARR_GC
							temp2[index]["PLAN"][0]["PD"][0]['D40_ACT_DIST']=PD_D40_ACT_DIST
							temp2[index]["PLAN"][0]["PD"][0]['D40_GC']=PD_D40_GC
							temp2[index]["PLAN"][0]["PD"][0]['D40_DIR_DIST']=PD_D40_DIR_DIST
							temp2[index]["PLAN"][0]["PD"][0]['A100_ACT_DIST']=PD_A100_ACT_DIST
							temp2[index]["PLAN"][0]["PD"][0]['A100_GC']=PD_A100_GC
							temp2[index]["PLAN"][0]["PD"][0]['A100_DIR_DIST']=PD_A100_DIR_DIST
							temp2[index]["PLAN"][0]["PD"][0]['A40_ACT_DIST']=PD_A40_ACT_DIST
							temp2[index]["PLAN"][0]["PD"][0]['A40_GC']=PD_A40_GC
							temp2[index]["PLAN"][0]["PD"][0]['A40_DIR_DIST']=PD_A40_DIR_DIST
							temp2[index]["PLAN"][0]["PD"][0]['ARR_ACT_DIST']=PD_ARR_ACT_DIST
							temp2[index]["PLAN"][0]["PD"][0]['ARR_GC']=PD_ARR_GC
							temp2[index]["PLAN"][0]["PD"][0]['ARR_DIR_DIST']=PD_ARR_DIR_DIST
					# working on LA 129-158
							#temp2["AIR"][0]['ARR_APRT'] = temp1_plan[130]	
							LA_ARR_APRT = temp1_plan[130]
							if temp1_plan[136] != '' and temp1_plan[137] != '' and temp1_plan[139] != '' and temp1_plan[140] != '' and temp1_plan[144] != '' and temp1_plan[145] != '' and temp1_plan[149] != '' and temp1_plan[150] != '' and temp1_plan[154] != '' and temp1_plan[155] != '':
								LA_DEP_coord = [-float(temp1_plan[137])/60, float(temp1_plan[136])/60]
								LA_D40_coord = [-float(temp1_plan[140])/60, float(temp1_plan[139])/60]
								LA_A100_coord = [-float(temp1_plan[145])/60,float(temp1_plan[144])/60]
								LA_A40_coord = [-float(temp1_plan[150])/60,float(temp1_plan[149])/60]		
								LA_ARR_coord = [-float(temp1_plan[155])/60,float(temp1_plan[154])/60]
							LA_WAYPT = temp1_plan[131]
							if temp1_plan[132]=='':
								LA_FPWAYPT = temp1_plan[132]
							elif temp1_plan[132]!='' and temp1_plan[132][0]==' ':
								LA_FPWAYPT = temp1_plan[132][1::]
							else: 
								LA_FPWAYPT = temp1_plan[132]
							LA_FIELD10 = temp1_plan[133]
							LA_DEPFIXID = temp1_plan[134]
							LA_ARRFIXID = temp1_plan[135]
							LA_DEP_ARR_GC = temp1_plan[138]
							LA_D40_ACT_DIST = temp1_plan[141]
							LA_D40_GC = temp1_plan[142]
							LA_D40_DIR_DIST = temp1_plan[143]
							LA_A100_ACT_DIST = temp1_plan[146]
							LA_A100_GC = temp1_plan[147]
							LA_A100_DIR_DIST = temp1_plan[148]
							LA_A40_ACT_DIST = temp1_plan[151]
							LA_A40_GC = temp1_plan[152]
							LA_A40_DIR_DIST = temp1_plan[153]
							LA_ARR_ACT_DIST= temp1_plan[156]	
							LA_ARR_GC = temp1_plan[157]
							LA_ARR_DIR_DIST	= temp1_plan[158]
							LA_WAYPT_coord = LA_WAYPT.split(' ')
							temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['type'] = 'linestring'
							temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'] = []
							if LA_WAYPT!= '':
								for i in range(0, len(LA_WAYPT_coord)):
									temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(LA_WAYPT_coord[i][5:9])/60)),(float(LA_WAYPT_coord[i][0:4])/60)])
							else:
								temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'].append(LA_WAYPT_coord)
								
							LA_FPWAYPT_coord = LA_FPWAYPT.split(' ')
							temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
							temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['coordinates'] = []
							if LA_FPWAYPT!= ' ':
								for i in range(1, len(LA_FPWAYPT_coord)):
									temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(LA_FPWAYPT_coord[i][5:9])/60)),(float(LA_FPWAYPT_coord[i][0:4])/60)])
							else:
								temp2["FPWAYPT_coord"][0]['coordinates'].append(LA_FPWAYPT_coord)
							temp2[index]["PLAN"][0]["LA"][0]['ARR_APRT'] = LA_ARR_APRT
							temp2[index]["PLAN"][0]["LA"][0]['DEP_coord']=LA_DEP_coord
							temp2[index]["PLAN"][0]["LA"][0]['D40_coord']=LA_D40_coord
							temp2[index]["PLAN"][0]["LA"][0]['A100_coord']=LA_A100_coord
							temp2[index]["PLAN"][0]["LA"][0]['A40_coord']=LA_A40_coord
							temp2[index]["PLAN"][0]["LA"][0]['ARR_coord']=LA_ARR_coord
							temp2[index]["PLAN"][0]["LA"][0]['WAYPT']=LA_WAYPT
							temp2[index]["PLAN"][0]["LA"][0]['FPWAYPT']=LA_FPWAYPT
							temp2[index]["PLAN"][0]["LA"][0]['FIELD10']=LA_FIELD10
							temp2[index]["PLAN"][0]["LA"][0]['DEPFIXID']=LA_DEPFIXID
							temp2[index]["PLAN"][0]["LA"][0]['ARRFIXID']=LA_ARRFIXID 
							temp2[index]["PLAN"][0]["LA"][0]['DEP_ARR_GC']=LA_DEP_ARR_GC
							temp2[index]["PLAN"][0]["LA"][0]['D40_ACT_DIST']=LA_D40_ACT_DIST
							temp2[index]["PLAN"][0]["LA"][0]['D40_GC']=LA_D40_GC
							temp2[index]["PLAN"][0]["LA"][0]['D40_DIR_DIST']=LA_D40_DIR_DIST
							temp2[index]["PLAN"][0]["LA"][0]['A100_ACT_DIST']=LA_A100_ACT_DIST
							temp2[index]["PLAN"][0]["LA"][0]['A100_GC']=LA_A100_GC
							temp2[index]["PLAN"][0]["LA"][0]['A100_DIR_DIST']=LA_A100_DIR_DIST
							temp2[index]["PLAN"][0]["LA"][0]['A40_ACT_DIST']=LA_A40_ACT_DIST
							temp2[index]["PLAN"][0]["LA"][0]['A40_GC']=LA_A40_GC
							temp2[index]["PLAN"][0]["LA"][0]['A40_DIR_DIST']=LA_A40_DIR_DIST
							temp2[index]["PLAN"][0]["LA"][0]['ARR_ACT_DIST']=LA_ARR_ACT_DIST
							temp2[index]["PLAN"][0]["LA"][0]['ARR_GC']=LA_ARR_GC
							temp2[index]["PLAN"][0]["LA"][0]['ARR_DIR_DIST']=LA_ARR_DIR_DIST
					#extra
							D40_A40_ACT_DIST = temp1_plan[159]
							D40_A40_GC_DIST	 = temp1_plan[160]
							D40_A40_DIR_DIST  = temp1_plan[161]
							D40_A40_ACH_DIST = temp1_plan[162]
							D40_A100_ACT_DIST = temp1_plan[163]
							D40_A100_GC_DIST= temp1_plan[164]
							D40_A100_DIR_DIST  = temp1_plan[165]
							D40_A100_ACH_DIST= temp1_plan[166]
							DEP_CENTER  = temp1_plan[167]
							DEP_CONUS= temp1_plan[168]
							ARR_CENTER  = temp1_plan[169]
							ARR_CONUS= temp1_plan[170]
							DEP_RANK  = temp1_plan[171]
							ARR_RANK= temp1_plan[172]
							LF_DIVERSION = temp1_plan[173]
							USER_CLASS = temp1_plan[174]
							ACFT_EQUIP  = temp1_plan[175]
							#FP_LF_FLAG  = temp1_plan[176]
							TZ_QUAL_FLAG = temp1_plan[177]
							temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_ACT_DIST'] = D40_A40_ACT_DIST
							temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_GC_DIST'] = D40_A40_GC_DIST
							temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_DIR_DIST'] = D40_A40_DIR_DIST
							temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_ACH_DIST'] = D40_A40_ACH_DIST
							temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_ACT_DIST'] = D40_A100_ACT_DIST
							temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_GC_DIST'] = D40_A100_GC_DIST
							temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_DIR_DIST'] = D40_A100_DIR_DIST
							temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_ACH_DIST'] = D40_A100_ACH_DIST
							temp2[index]["PLAN"][0]["AIR"][0]['DEP_CENTER'] = DEP_CENTER
							temp2[index]["PLAN"][0]["AIR"][0]['DEP_CONUS'] = DEP_CONUS
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_CENTER'] = ARR_CENTER
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_CONUS'] = ARR_CONUS
							temp2[index]["PLAN"][0]["AIR"][0]['DEP_RANK'] = DEP_RANK
							temp2[index]["PLAN"][0]["AIR"][0]['ARR_RANK'] = ARR_RANK
							temp2[index]["PLAN"][0]["AIR"][0]['LF_DIVERSION'] = LF_DIVERSION
							temp2[index]["PLAN"][0]["AIR"][0]['USER_CLASS'] = USER_CLASS
							temp2[index]["PLAN"][0]["AIR"][0]['ACFT_EQUIP'] = ACFT_EQUIP
							#temp2[index]["PLAN"][0]["AIR"][0] = FP_LF_FLAG
							temp2[index]["PLAN"][0]["AIR"][0]['TZ_QUAL_FLAG'] = TZ_QUAL_FLAG
							###### end code
							fid3.close()
							break
						else:
							found_plan = 0					
					if found_plan == 0:
						fid4 = open('FLIGHT_PLAN_EN_CP_2013_part3.csv', 'rb')
						r4, n4 = 0, 0
						found_plan = 0
						for row4 in fid4:
							row4 = row4.replace('\r\n', '')
							row4 = row4.replace('"', '')
							if r == 0:
								field4 = row4.split(',')
								r += 1
							else:
								temp1_plan = row4.split(',')
								uniqueList_plan = temp1_plan[1] +'_'+temp1_plan[0] +'_'+temp1_plan[2]
							if uniqueList_plan == (temp1[2] +'_'+temp1[3] +'_'+temp1[4]):
								found_plan = 1
								######insert code	
								temp2[index]["PLAN"]=[]
								temp2[index]["PLAN"].append({})
								temp2[index]["PLAN"][0]["LF"]=[]
								temp2[index]["PLAN"][0]["LF"].append({})
								temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"] = []
								temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"].append({})
								temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"] = []
								temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"].append({})
								temp2[index]["PLAN"][0]["PD"] = []
								temp2[index]["PLAN"][0]["PD"].append({})
								temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"] = []
								temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"].append({})
								temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"] = []
								temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"].append({})
								temp2[index]["PLAN"][0]["LA"] = []
								temp2[index]["PLAN"][0]["LA"].append({})
								temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"] = []
								temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"].append({})
								temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"] = []
								temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"].append({})
								temp2[index]["PLAN"][0]["AIR"]=[]
								temp2[index]["PLAN"][0]["AIR"].append({})
								# ORIG 0-68
								date = temp1_plan[0]
								acid = temp1_plan[1]
								ARR_APRT = temp1_plan[4]
								D40_coord = [-float(temp1_plan[6])/60, float(temp1_plan[5])/60]
								D40_alt = temp1_plan[7]
								D40_time = temp1_plan[8]
								D40_distflown = temp1_plan[9]
								D40_dura = temp1_plan[10]
								D40_bear_from_aprt = temp1_plan[11]
								D40_GCD = temp1_plan[12]
								D40_CF = temp1_plan[13]
								D100_coord = [-float(temp1_plan[15])/60, float(temp1_plan[14])/60]
								D100_alt = temp1_plan[16]
								D100_time = temp1_plan[17]
								D100_distflown = temp1_plan[18]
								D100_dura = temp1_plan[19]
								D100_bear_from_aprt = temp1_plan[20]
								D100_CGD = temp1_plan[21]
								D100_CF = temp1_plan[22]
								if temp1_plan[24]!= '' and temp1_plan[23] != '':
									A200_coord = [-float(temp1_plan[24])/60, float(temp1_plan[23])/60]
								else:
									A200_coord =''
								A200_alt = temp1_plan[25]
								temp2[index]["PLAN"][0]["AIR"][0]['ALTITUDE']=temp1_plan[57]
								temp2[index]["PLAN"][0]["AIR"][0]['A200_ALT']=A200_alt
								A200_time = temp1_plan[26]
								A200_distflown = temp1_plan[27]
								A200_dura = temp1_plan[28]
								A200_bear_from_aprt = temp1_plan[29]
								A200_CGD = temp1_plan[30]
								A200_CF = temp1_plan[31]
								A100_coord = [-float(temp1_plan[33])/60,float(temp1_plan[32])/60]
								A100_alt = temp1_plan[34]
								temp2[index]["PLAN"][0]["AIR"][0]['A100_ALT']=A100_alt
								A100_time = temp1_plan[35]
								A100_distflown = temp1_plan[36]
								A100_dura = temp1_plan[37]
								A100_bear_from_aprt = temp1_plan[38]
								A100_CGD = temp1_plan[39]
								A100_CF = temp1_plan[40]
								
								
								A40_coord = [-float(temp1_plan[42])/60,float(temp1_plan[41])/60]
								A40_alt = temp1_plan[43]
								temp2[index]["PLAN"][0]["AIR"][0]['A40_ALT']=A40_alt
								A40_time = temp1_plan[44]
								A40_distflown = temp1_plan[45]
								A40_dura = temp1_plan[46]
								A40_bear_from_aprt = temp1_plan[47]
								A40_CGD = temp1_plan[48]
								A40_CF = temp1_plan[49]
								##
								temp2[index]["PLAN"][0]["AIR"][0]['ACT_DATE'] = temp1_plan[0]
								temp2[index]["PLAN"][0]["AIR"][0]['ARL_COD'] = acid[0:3]
								temp2[index]["PLAN"][0]["AIR"][0]['FLI_NUM'] = acid[3::]
								temp2[index]["PLAN"][0]["AIR"][0]['FLIGHT_INDEX'] = temp1_plan[2]
								temp2[index]["PLAN"][0]["AIR"][0]['DEP_APRT'] = temp1_plan[3]
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_APRT'] = ARR_APRT
								temp2[index]["PLAN"][0]["AIR"][0]['D40_coord'] = D40_coord
								temp2[index]["PLAN"][0]["AIR"][0]['D40_ALT']=D40_alt
								temp2[index]["PLAN"][0]["AIR"][0]['D40_distflown'] = D40_distflown
								temp2[index]["PLAN"][0]["AIR"][0]['D40_dura'] = D40_dura
								temp2[index]["PLAN"][0]["AIR"][0]['D40_bear_from_aprt'] = D40_bear_from_aprt
								temp2[index]["PLAN"][0]["AIR"][0]['D40_GCD'] = D40_GCD
								temp2[index]["PLAN"][0]["AIR"][0]['D40_CF'] = D40_CF
								temp2[index]["PLAN"][0]["AIR"][0]['D100_coord'] = D100_coord
								temp2[index]["PLAN"][0]["AIR"][0]['D100_ALT']=D100_alt
								temp2[index]["PLAN"][0]["AIR"][0]['D100_distflown'] = D100_distflown
								temp2[index]["PLAN"][0]["AIR"][0]['D100_dura'] = D100_dura
								temp2[index]["PLAN"][0]["AIR"][0]['D100_bear_from_aprt'] = D100_bear_from_aprt
								temp2[index]["PLAN"][0]["AIR"][0]['D100_CGD'] = D100_CGD
								temp2[index]["PLAN"][0]["AIR"][0]['D100_CF'] = D100_CF
								temp2[index]["PLAN"][0]["AIR"][0]['A200_coord'] = A200_coord
								temp2[index]["PLAN"][0]["AIR"][0]['A200_distflown'] = A200_distflown 
								temp2[index]["PLAN"][0]["AIR"][0]['A200_dura'] = A200_dura
								temp2[index]["PLAN"][0]["AIR"][0]['A200_bear_from_aprt'] = A200_bear_from_aprt
								temp2[index]["PLAN"][0]["AIR"][0]['A200_CGD'] = A200_CGD 
								temp2[index]["PLAN"][0]["AIR"][0]['A200_CF'] = A200_CF 
								temp2[index]["PLAN"][0]["AIR"][0]['A100_coord'] = A100_coord 
								temp2[index]["PLAN"][0]["AIR"][0]['A100_distflown'] = A100_distflown 
								temp2[index]["PLAN"][0]["AIR"][0]['A100_dura'] = A100_dura
								temp2[index]["PLAN"][0]["AIR"][0]['A100_bear_from_aprt'] = A100_bear_from_aprt 
								temp2[index]["PLAN"][0]["AIR"][0]['A100_CGD'] = A100_CGD
								temp2[index]["PLAN"][0]["AIR"][0]['A100_CF'] = A100_CF 		
								temp2[index]["PLAN"][0]["AIR"][0]['A40_coord'] = A40_coord
								temp2[index]["PLAN"][0]["AIR"][0]['A40_distflown'] = A40_distflown
								temp2[index]["PLAN"][0]["AIR"][0]['A40_dura'] = A40_dura 
								temp2[index]["PLAN"][0]["AIR"][0]['A40_bear_from_aprt'] = A40_bear_from_aprt 
								temp2[index]["PLAN"][0]["AIR"][0]['A40_CGD'] = A40_CGD
								temp2[index]["PLAN"][0]["AIR"][0]['A40_CF'] = A40_CF 
								##
								temp2[index]["PLAN"][0]["AIR"][0]['D40_TIME']=(D40_time)[9::]
								temp2[index]["PLAN"][0]["AIR"][0]['D100_TIME']=(D100_time)[9::]
								temp2[index]["PLAN"][0]["AIR"][0]['A200_TIME']=(A200_time)[9::]
								temp2[index]["PLAN"][0]["AIR"][0]['A100_TIME']=(A100_time)[9::]
								temp2[index]["PLAN"][0]["AIR"][0]['A40_TIME']=(A40_time)[9::]
								temp2[index]["PLAN"][0]["AIR"][0]['D40_DATE']=(D40_time)[0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['D100_DATE']=(D100_time)[0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['A200_DATE']=(A200_time)[0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['A100_DATE']=(A100_time)[0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['A40_DATE']=(A40_time)[0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_TIME'] = temp1_plan[50][9::]
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_DATE'] = temp1_plan[50][0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_distflown'] = temp1_plan[51]
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_dura'] = temp1_plan[52]
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_GCD'] = temp1_plan[53]
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_CF'] = temp1_plan[54]
								
						#FP ---------------------------------------------------------------------------------------------------------------------------		
								#FP_DEPT_TIME = temp1_plan[55]
								temp2[index]["PLAN"][0]["AIR"][0]['FP_DEP_TIME'] = temp1_plan[55][9::]
								temp2[index]["PLAN"][0]["AIR"][0]['FP_DEP_DATE'] = temp1_plan[55][0:8]
								#FP_ARR_TIME = temp1_plan[56]
								temp2[index]["PLAN"][0]["AIR"][0]['FP_ARR_TIME'] = temp1_plan[56][9::]
								temp2[index]["PLAN"][0]["AIR"][0]['FP_ARR_DATE'] = temp1_plan[56][0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['SPEED'] = temp1_plan[58]
								temp2[index]["PLAN"][0]["AIR"][0]['ACFT_TYPE'] = temp1_plan[59]
								temp2[index]["PLAN"][0]["AIR"][0]['PHYSICAL_CLASS'] = temp1_plan[60]
								temp2[index]["PLAN"][0]["AIR"][0]['USER_CLASS'] = temp1_plan[61]
								temp2[index]["PLAN"][0]["AIR"][0]['SCHED_DEP_DATE'] = temp1_plan[62][0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['SCHED_DEP_TIME'] = temp1_plan[62][9::]
								temp2[index]["PLAN"][0]["AIR"][0]['SCHED_ARR_DATE'] = temp1_plan[63][0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['SCHED_ARR_TIME'] = temp1_plan[63][9::]
								temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_DEP_DATE'] = temp1_plan[64][0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_DEP_TIME'] = temp1_plan[64][9::]
								temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_ARR_DATE'] = temp1_plan[65][0:8]
								temp2[index]["PLAN"][0]["AIR"][0]['ACTUAL_ARR_TIME'] = temp1_plan[65][9::]
								temp2[index]["PLAN"][0]["AIR"][0]['PRE_DEP_AMENDS'] = temp1_plan[66]
								temp2[index]["PLAN"][0]["AIR"][0]['POST_DEP_AMEND'] = temp1_plan[67]
								temp2[index]["PLAN"][0]["AIR"][0]['MSG_ORIG_TIME'] = temp1_plan[68]	
								
						# working on LF 69-98---------------------------------------------------------------------------------------------------------------------------		
								LF_ARR_APRT = temp1_plan[70]
								if temp1_plan[76] != '' and temp1_plan[77] != '' and temp1_plan[79] != '' and temp1_plan[80] != '' and temp1_plan[84] != '' and temp1_plan[85] != '' and temp1_plan[89] != '' and temp1_plan[90] != '' and temp1_plan[94] != '' and temp1_plan[95] != '':
									LF_DEP_coord = [-float(temp1_plan[77])/60, float(temp1_plan[76])/60]
									LF_D40_coord = [-float(temp1_plan[80])/60, float(temp1_plan[79])/60]
									LF_A100_coord = [-float(temp1_plan[85])/60,float(temp1_plan[84])/60]
									LF_A40_coord = [-float(temp1_plan[90])/60,float(temp1_plan[89])/60]
									LF_ARR_coord = [-float(temp1_plan[95])/60,float(temp1_plan[94])/60]
								LF_WAYPT = temp1_plan[71]
								if temp1_plan[72]=='':
									LF_FPWAYPT = temp1_plan[72]
								elif temp1_plan[72]!='' and temp1_plan[72][0]==' ':
									LF_FPWAYPT = temp1_plan[72][1::]	
								else: 
									LF_FPWAYPT = temp1_plan[72]

								LF_WAYPT_coord = LF_WAYPT.split(' ')
								temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['type'] = 'linestring'
								temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'] = []
								if LF_WAYPT!= '':
									for i in range(0, len(LF_WAYPT_coord)):
										temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(LF_WAYPT_coord[i][5:9])/60)),(float(LF_WAYPT_coord[i][0:4])/60)])
								else:
									temp2[index]["PLAN"][0]["LF"][0]["WAYPT_coord"][0]['coordinates'].append(LF_WAYPT_coord)
									
								LF_FPWAYPT_coord = LF_FPWAYPT.split(' ')
								temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
								temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'] = []
								a=LF_FPWAYPT_coord[0][5:9]
								b=LF_FPWAYPT_coord[0][0:4]
								if LF_FPWAYPT!= ' ':
									for i in range(1, len(LF_FPWAYPT_coord)):
										temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(LF_FPWAYPT_coord[i][5:9])/60)),(float(LF_FPWAYPT_coord[i][0:4])/60)])
								else:
									temp2[index]["PLAN"][0]["LF"][0]["FPWAYPT_coord"][0]['coordinates'].append(LF_FPWAYPT_coord)
								
								LF_FIELD10 = temp1_plan[73]
								LF_DEPFIXID = temp1_plan[74]
								LF_ARRFIXID = temp1_plan[75]
								LF_DEP_ARR_GC = temp1_plan[78]
								LF_D40_ACT_DIST = temp1_plan[81]
								LF_D40_GC = temp1_plan[82]
								LF_D40_DIR_DIST = temp1_plan[83]
								LF_A100_ACT_DIST = temp1_plan[86]
								LF_A100_GC = temp1_plan[87]
								LF_A100_DIR_DIST = temp1_plan[88]
								LF_A40_ACT_DIST	= temp1_plan[91]
								LF_A40_GC = temp1_plan[92]
								LF_A40_DIR_DIST = temp1_plan[93]
								LF_ARR_ACT_DIST	= temp1_plan[96]
								LF_ARR_GC = temp1_plan[97]	
								LF_ARR_DIR_DIST = temp1_plan[98]	
								temp2[index]["PLAN"][0]["LF"][0]['ARR_APRT'] = LF_ARR_APRT
								temp2[index]["PLAN"][0]["LF"][0]['DEP_coord']=LF_DEP_coord
								temp2[index]["PLAN"][0]["LF"][0]['D40_coord']=LF_D40_coord
								temp2[index]["PLAN"][0]["LF"][0]['A100_coord']=LF_A100_coord
								temp2[index]["PLAN"][0]["LF"][0]['A40_coord']=LF_A40_coord
								temp2[index]["PLAN"][0]["LF"][0]['ARR_coord']=LF_ARR_coord
								temp2[index]["PLAN"][0]["LF"][0]['WAYPT']=LF_WAYPT
								temp2[index]["PLAN"][0]["LF"][0]['FPWAYPT']=LF_FPWAYPT
								temp2[index]["PLAN"][0]["LF"][0]['FIELD10']=LF_FIELD10
								temp2[index]["PLAN"][0]["LF"][0]['DEPFIXID']=LF_DEPFIXID
								temp2[index]["PLAN"][0]["LF"][0]['ARRFIXID']=LF_ARRFIXID 
								temp2[index]["PLAN"][0]["LF"][0]['DEP_ARR_GC']=LF_DEP_ARR_GC
								temp2[index]["PLAN"][0]["LF"][0]['D40_ACT_DIST']=LF_D40_ACT_DIST
								temp2[index]["PLAN"][0]["LF"][0]['D40_GC']=LF_D40_GC
								temp2[index]["PLAN"][0]["LF"][0]['D40_DIR_DIST']=LF_D40_DIR_DIST
								temp2[index]["PLAN"][0]["LF"][0]['A100_ACT_DIST']=LF_A100_ACT_DIST
								temp2[index]["PLAN"][0]["LF"][0]['A100_GC']=LF_A100_GC
								temp2[index]["PLAN"][0]["LF"][0]['A100_DIR_DIST']=LF_A100_DIR_DIST
								temp2[index]["PLAN"][0]["LF"][0]['A40_ACT_DIST']=LF_A40_ACT_DIST
								temp2[index]["PLAN"][0]["LF"][0]['A40_GC']=LF_A40_GC
								temp2[index]["PLAN"][0]["LF"][0]['A40_DIR_DIST']=LF_A40_DIR_DIST
								temp2[index]["PLAN"][0]["LF"][0]['ARR_ACT_DIST']=LF_ARR_ACT_DIST
								temp2[index]["PLAN"][0]["LF"][0]['ARR_GC']=LF_ARR_GC
								temp2[index]["PLAN"][0]["LF"][0]['ARR_DIR_DIST']=LF_ARR_DIR_DIST
								
								
						# working on PD 99-128---------------------------------------------------------------------------------------------------------------------------		
								PD_ARR_APRT = temp1_plan[100]
								if temp1_plan[106] != '' and temp1_plan[107] != '' and temp1_plan[109] != '' and temp1_plan[110] != '' and temp1_plan[114] != '' and temp1_plan[115] != '' and temp1_plan[119] != '' and temp1_plan[120] != '' and temp1_plan[124] != '' and temp1_plan[125] != '':
									PD_DEP_coord = [-float(temp1_plan[107])/60, float(temp1_plan[106])/60]
									PD_D40_coord = [-float(temp1_plan[110])/60, float(temp1_plan[109])/60]
									PD_A100_coord = [-float(temp1_plan[115])/60,float(temp1_plan[114])/60]
									PD_A40_coord = [-float(temp1_plan[120])/60,float(temp1_plan[119])/60]
									PD_ARR_coord = [-float(temp1_plan[125])/60,float(temp1_plan[124])/60]
								PD_WAYPT = temp1_plan[101]
								if temp1_plan[102]=='':
									PD_FPWAYPT = temp1_plan[102]
								elif temp1_plan[102]!='' and temp1_plan[102][0]=='':
									PD_FPWAYPT = temp1_plan[102][1::]	
								else: 
									PD_FPWAYPT = temp1_plan[102]
								PD_FIELD10 = temp1_plan[103]
								PD_DEPFIXID = temp1_plan[104]
								PD_ARRFIXID = temp1_plan[105]
								PD_DEP_ARR_GC = temp1_plan[108]
								PD_D40_ACT_DIST = temp1_plan[111]
								PD_D40_GC = temp1_plan[112]
								PD_D40_DIR_DIST = temp1_plan[113]
								PD_A100_ACT_DIST = temp1_plan[116]
								PD_A100_GC = temp1_plan[117]
								PD_A100_DIR_DIST = temp1_plan[118]
								PD_A40_ACT_DIST = temp1_plan[121]
								PD_A40_GC = temp1_plan[122]
								PD_A40_DIR_DIST = temp1_plan[123]
								PD_ARR_ACT_DIST =temp1_plan[126]
								PD_ARR_GC = temp1_plan[127]
								PD_ARR_DIR_DIST = temp1_plan[128]
								
								PD_WAYPT_coord = PD_WAYPT.split(' ')
								temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['type'] = 'linestring'
								temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'] = []
								if PD_WAYPT!= '':
									for i in range(0, len(PD_WAYPT_coord)):
										temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(PD_WAYPT_coord[i][5:9])/60)),(float(PD_WAYPT_coord[i][0:4])/60)])
								else:
									temp2[index]["PLAN"][0]["PD"][0]["WAYPT_coord"][0]['coordinates'].append(PD_WAYPT_coord)
									
								PD_FPWAYPT_coord = PD_FPWAYPT.split(' ')
								temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
								temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'] = []
								if PD_FPWAYPT!= ' ':
									for i in range(1, len(PD_FPWAYPT_coord)):
										temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(PD_FPWAYPT_coord[i][5:9])/60)),(float(PD_FPWAYPT_coord[i][0:4])/60)])
								else:
									temp2[index]["PLAN"][0]["PD"][0]["FPWAYPT_coord"][0]['coordinates'].append(PD_FPWAYPT_coord)
								temp2[index]["PLAN"][0]["PD"][0]['ARR_APRT'] = PD_ARR_APRT
								temp2[index]["PLAN"][0]["PD"][0]['DEP_coord']=PD_DEP_coord
								temp2[index]["PLAN"][0]["PD"][0]['D40_coord']=PD_D40_coord
								temp2[index]["PLAN"][0]["PD"][0]['A100_coord']=PD_A100_coord
								temp2[index]["PLAN"][0]["PD"][0]['A40_coord']=PD_A40_coord
								temp2[index]["PLAN"][0]["PD"][0]['ARR_coord']=PD_ARR_coord
								temp2[index]["PLAN"][0]["PD"][0]['WAYPT']=PD_WAYPT
								temp2[index]["PLAN"][0]["PD"][0]['FPWAYPT']=PD_FPWAYPT
								temp2[index]["PLAN"][0]["PD"][0]['FIELD10']=PD_FIELD10
								temp2[index]["PLAN"][0]["PD"][0]['DEPFIXID']=PD_DEPFIXID
								temp2[index]["PLAN"][0]["PD"][0]['ARRFIXID']=PD_ARRFIXID 
								temp2[index]["PLAN"][0]["PD"][0]['DEP_ARR_GC']=PD_DEP_ARR_GC
								temp2[index]["PLAN"][0]["PD"][0]['D40_ACT_DIST']=PD_D40_ACT_DIST
								temp2[index]["PLAN"][0]["PD"][0]['D40_GC']=PD_D40_GC
								temp2[index]["PLAN"][0]["PD"][0]['D40_DIR_DIST']=PD_D40_DIR_DIST
								temp2[index]["PLAN"][0]["PD"][0]['A100_ACT_DIST']=PD_A100_ACT_DIST
								temp2[index]["PLAN"][0]["PD"][0]['A100_GC']=PD_A100_GC
								temp2[index]["PLAN"][0]["PD"][0]['A100_DIR_DIST']=PD_A100_DIR_DIST
								temp2[index]["PLAN"][0]["PD"][0]['A40_ACT_DIST']=PD_A40_ACT_DIST
								temp2[index]["PLAN"][0]["PD"][0]['A40_GC']=PD_A40_GC
								temp2[index]["PLAN"][0]["PD"][0]['A40_DIR_DIST']=PD_A40_DIR_DIST
								temp2[index]["PLAN"][0]["PD"][0]['ARR_ACT_DIST']=PD_ARR_ACT_DIST
								temp2[index]["PLAN"][0]["PD"][0]['ARR_GC']=PD_ARR_GC
								temp2[index]["PLAN"][0]["PD"][0]['ARR_DIR_DIST']=PD_ARR_DIR_DIST
						# working on LA 129-158
								#temp2["AIR"][0]['ARR_APRT'] = temp1_plan[130]	
								LA_ARR_APRT = temp1_plan[130]
								if temp1_plan[136] != '' and temp1_plan[137] != '' and temp1_plan[139] != '' and temp1_plan[140] != '' and temp1_plan[144] != '' and temp1_plan[145] != '' and temp1_plan[149] != '' and temp1_plan[150] != '' and temp1_plan[154] != '' and temp1_plan[155] != '':
									LA_DEP_coord = [-float(temp1_plan[137])/60, float(temp1_plan[136])/60]
									LA_D40_coord = [-float(temp1_plan[140])/60, float(temp1_plan[139])/60]
									LA_A100_coord = [-float(temp1_plan[145])/60,float(temp1_plan[144])/60]
									LA_A40_coord = [-float(temp1_plan[150])/60,float(temp1_plan[149])/60]		
									LA_ARR_coord = [-float(temp1_plan[155])/60,float(temp1_plan[154])/60]
								LA_WAYPT = temp1_plan[131]
								if temp1_plan[132]=='':
									LA_FPWAYPT = temp1_plan[132]
								elif temp1_plan[132]!='' and temp1_plan[132][0]==' ':
									LA_FPWAYPT = temp1_plan[132][1::]
								else: 
									LA_FPWAYPT = temp1_plan[132]
								LA_FIELD10 = temp1_plan[133]
								LA_DEPFIXID = temp1_plan[134]
								LA_ARRFIXID = temp1_plan[135]
								LA_DEP_ARR_GC = temp1_plan[138]
								LA_D40_ACT_DIST = temp1_plan[141]
								LA_D40_GC = temp1_plan[142]
								LA_D40_DIR_DIST = temp1_plan[143]
								LA_A100_ACT_DIST = temp1_plan[146]
								LA_A100_GC = temp1_plan[147]
								LA_A100_DIR_DIST = temp1_plan[148]
								LA_A40_ACT_DIST = temp1_plan[151]
								LA_A40_GC = temp1_plan[152]
								LA_A40_DIR_DIST = temp1_plan[153]
								LA_ARR_ACT_DIST= temp1_plan[156]	
								LA_ARR_GC = temp1_plan[157]
								LA_ARR_DIR_DIST	= temp1_plan[158]
								LA_WAYPT_coord = LA_WAYPT.split(' ')
								temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['type'] = 'linestring'
								temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'] = []
								if LA_WAYPT!= '':
									for i in range(0, len(LA_WAYPT_coord)):
										temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'].append([(-(float(LA_WAYPT_coord[i][5:9])/60)),(float(LA_WAYPT_coord[i][0:4])/60)])
								else:
									temp2[index]["PLAN"][0]["LA"][0]["WAYPT_coord"][0]['coordinates'].append(LA_WAYPT_coord)
									
								LA_FPWAYPT_coord = LA_FPWAYPT.split(' ')
								temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['type'] = 'linestring'
								temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['coordinates'] = []
								if LA_FPWAYPT!= ' ':
									for i in range(1, len(LA_FPWAYPT_coord)):
										temp2[index]["PLAN"][0]["LA"][0]["FPWAYPT_coord"][0]['coordinates'].append([(-(float(LA_FPWAYPT_coord[i][5:9])/60)),(float(LA_FPWAYPT_coord[i][0:4])/60)])
								else:
									temp2["FPWAYPT_coord"][0]['coordinates'].append(LA_FPWAYPT_coord)
								temp2[index]["PLAN"][0]["LA"][0]['ARR_APRT'] = LA_ARR_APRT
								temp2[index]["PLAN"][0]["LA"][0]['DEP_coord']=LA_DEP_coord
								temp2[index]["PLAN"][0]["LA"][0]['D40_coord']=LA_D40_coord
								temp2[index]["PLAN"][0]["LA"][0]['A100_coord']=LA_A100_coord
								temp2[index]["PLAN"][0]["LA"][0]['A40_coord']=LA_A40_coord
								temp2[index]["PLAN"][0]["LA"][0]['ARR_coord']=LA_ARR_coord
								temp2[index]["PLAN"][0]["LA"][0]['WAYPT']=LA_WAYPT
								temp2[index]["PLAN"][0]["LA"][0]['FPWAYPT']=LA_FPWAYPT
								temp2[index]["PLAN"][0]["LA"][0]['FIELD10']=LA_FIELD10
								temp2[index]["PLAN"][0]["LA"][0]['DEPFIXID']=LA_DEPFIXID
								temp2[index]["PLAN"][0]["LA"][0]['ARRFIXID']=LA_ARRFIXID 
								temp2[index]["PLAN"][0]["LA"][0]['DEP_ARR_GC']=LA_DEP_ARR_GC
								temp2[index]["PLAN"][0]["LA"][0]['D40_ACT_DIST']=LA_D40_ACT_DIST
								temp2[index]["PLAN"][0]["LA"][0]['D40_GC']=LA_D40_GC
								temp2[index]["PLAN"][0]["LA"][0]['D40_DIR_DIST']=LA_D40_DIR_DIST
								temp2[index]["PLAN"][0]["LA"][0]['A100_ACT_DIST']=LA_A100_ACT_DIST
								temp2[index]["PLAN"][0]["LA"][0]['A100_GC']=LA_A100_GC
								temp2[index]["PLAN"][0]["LA"][0]['A100_DIR_DIST']=LA_A100_DIR_DIST
								temp2[index]["PLAN"][0]["LA"][0]['A40_ACT_DIST']=LA_A40_ACT_DIST
								temp2[index]["PLAN"][0]["LA"][0]['A40_GC']=LA_A40_GC
								temp2[index]["PLAN"][0]["LA"][0]['A40_DIR_DIST']=LA_A40_DIR_DIST
								temp2[index]["PLAN"][0]["LA"][0]['ARR_ACT_DIST']=LA_ARR_ACT_DIST
								temp2[index]["PLAN"][0]["LA"][0]['ARR_GC']=LA_ARR_GC
								temp2[index]["PLAN"][0]["LA"][0]['ARR_DIR_DIST']=LA_ARR_DIR_DIST
						#extra
								D40_A40_ACT_DIST = temp1_plan[159]
								D40_A40_GC_DIST	 = temp1_plan[160]
								D40_A40_DIR_DIST  = temp1_plan[161]
								D40_A40_ACH_DIST = temp1_plan[162]
								D40_A100_ACT_DIST = temp1_plan[163]
								D40_A100_GC_DIST= temp1_plan[164]
								D40_A100_DIR_DIST  = temp1_plan[165]
								D40_A100_ACH_DIST= temp1_plan[166]
								DEP_CENTER  = temp1_plan[167]
								DEP_CONUS= temp1_plan[168]
								ARR_CENTER  = temp1_plan[169]
								ARR_CONUS= temp1_plan[170]
								DEP_RANK  = temp1_plan[171]
								ARR_RANK= temp1_plan[172]
								LF_DIVERSION = temp1_plan[173]
								USER_CLASS = temp1_plan[174]
								ACFT_EQUIP  = temp1_plan[175]
								#FP_LF_FLAG  = temp1_plan[176]
								TZ_QUAL_FLAG = temp1_plan[177]
								temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_ACT_DIST'] = D40_A40_ACT_DIST
								temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_GC_DIST'] = D40_A40_GC_DIST
								temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_DIR_DIST'] = D40_A40_DIR_DIST
								temp2[index]["PLAN"][0]["AIR"][0]['D40_A40_ACH_DIST'] = D40_A40_ACH_DIST
								temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_ACT_DIST'] = D40_A100_ACT_DIST
								temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_GC_DIST'] = D40_A100_GC_DIST
								temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_DIR_DIST'] = D40_A100_DIR_DIST
								temp2[index]["PLAN"][0]["AIR"][0]['D40_A100_ACH_DIST'] = D40_A100_ACH_DIST
								temp2[index]["PLAN"][0]["AIR"][0]['DEP_CENTER'] = DEP_CENTER
								temp2[index]["PLAN"][0]["AIR"][0]['DEP_CONUS'] = DEP_CONUS
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_CENTER'] = ARR_CENTER
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_CONUS'] = ARR_CONUS
								temp2[index]["PLAN"][0]["AIR"][0]['DEP_RANK'] = DEP_RANK
								temp2[index]["PLAN"][0]["AIR"][0]['ARR_RANK'] = ARR_RANK
								temp2[index]["PLAN"][0]["AIR"][0]['LF_DIVERSION'] = LF_DIVERSION
								temp2[index]["PLAN"][0]["AIR"][0]['USER_CLASS'] = USER_CLASS
								temp2[index]["PLAN"][0]["AIR"][0]['ACFT_EQUIP'] = ACFT_EQUIP
								#temp2[index]["PLAN"][0]["AIR"][0] = FP_LF_FLAG
								temp2[index]["PLAN"][0]["AIR"][0]['TZ_QUAL_FLAG'] = TZ_QUAL_FLAG
								###### end code								
								fid4.close()								
								break
							else:
								found_plan = 0
				
				
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