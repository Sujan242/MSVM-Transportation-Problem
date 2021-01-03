import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
data= pd.read_csv('input.csv')

output=[]
costs_list=[]
for instance in range(1):
	print(instance+1)
	costs=ast.literal_eval(data['Costs'].iloc[instance])
	demand=ast.literal_eval(data['Demand'].iloc[instance])
	supply=ast.literal_eval(data['Supply'].iloc[instance])
	cols = sorted(demand.keys())
	costs1=copy.deepcopy(costs)
	supply1= copy.deepcopy(supply)
	demand1 = copy.deepcopy(demand)
	# for s in supply1:
	# 	dummy=True
	# 	for d in demand:
	# 		if costs[s][d]!=0:
	# 			dummy=False
	# 			break
	# 	if dummy==True:
	# 		del costs[s]
	# 		del supply[s]

	# for d in demand1:
	# 	dummy=True
	# 	for s in supply:
	# 		if costs[s][d]!=0:
	# 			dummy=False
	# 			break
	# 	if dummy==True:
	# 		for s in supply:
	# 			del costs[s][d]
	# 		del demand[d]
	costs1=copy.deepcopy(costs)
	unbalanced = False
	if sum(supply.values())!=sum(demand.values()):
		unbalanced=True

	status = {}
	for s in supply.keys():  #step 1
		status[s]="NS"

	res = {}
	for s in supply:
		res[s]={}
		for d in demand:
			res[s][d]=0
	count =0 
	step3 = False

	alloc = res

	for d in demand:  #step 2
		mn=1000000000
		mns = "S"
		for s in supply:
			if costs[s][d]<mn:
				mn=costs[s][d]
				mns=s
		alloc[mns][d] = min(demand[d] , supply[mns])
		# print(mns , d)
	res=alloc

	# print(alloc)

	while True:
		count+=1
		# print(demand)
		# if count>=6:
		# 	break
		alloc = res
		# print(res)
		# print()
		
		# if step3==False:
		# print(listsupply.keys())
		if True:
			res = alloc
			er=list(supply.keys())[0]
			for s in supply:  #step 3
				alc = 0
				for d in demand:
					alc += alloc[s][d]
				if alc>=supply[s]:
					# print(alc)
					status[s]="ER"
					er=s 
		# print(er)
		# status[er] = "ER"


		flr=list(supply.keys())[0]
		slr=list(supply.keys())[1]
		min_diff=100000000000
		column_with_min_diff="D"
		for d in demand:
			if demand[d]!=0:
				column_with_min_diff = d 
				break

		for d in demand:  #step 5
			# if demand[d]==0:
			# 	continue
			if alloc[er][d]!=0:
				mns="S"
				mn=100000
				for s in supply:
					if costs[s][d]<mn:
						mn=costs[s][d]
						mns = s
				mns2="S"
				mn2=1000000
				for s in supply:
					if costs[s][d]<mn2 and s!=mns:
						mn2=costs[s][d]
						mns2=s
				# print(mn2-mn)
				if mn2 - mn < min_diff:
					min_diff = mn2- mn
					flr = mns
					slr = mns2
					column_with_min_diff = d
		# print(er,flr , slr , column_with_min_diff , min_diff)

		# print(alloc)
		# print()
		# print(costs)
		# print()
		# print(supply)
		# print()
		# print(demand)
		# print()
		# if min_diff==0:
		# 	print(alloc)
		# 	print(supply)
		# 	print(costs)
		# 	print(demand)
		# 	exit()
		# print(res)
		if unbalanced==True: #step 6
			tunflr = 0
			for d in demand:
				tunflr+= (res[flr][d] - res[slr][d])

			if status[slr]=="ER" or tunflr<=supply[flr]:
				#step 9
				max_supply = supply[flr]
				max_demand = demand[column_with_min_diff]

				for d in demand:
					max_supply -= res[flr][d]

				for s in supply:
					max_demand -= res[s][column_with_min_diff]

				max_demand+= res[flr][column_with_min_diff]
				max_demand+= res[slr][column_with_min_diff]

				max_supply+= res[flr][column_with_min_diff]

				# print(max_supply , max_demand)

				max_alloc = min(max_supply , max_demand)
				max_alloc=max(max_alloc , 0 )

				res[flr][column_with_min_diff] = max_alloc  #step 13

				res[slr][column_with_min_diff] += demand[column_with_min_diff] - max_alloc

				# print(res)
				# if column_with_min_diff=="D1":
				# 	print("show")
				demand[column_with_min_diff]=0
				tuflr=0
				for d in demand:
					tuflr += res[flr][d]

				if tuflr == supply[flr]:  #step 14
					# for d in demand:
					# 	demand[d] - res[flr][d]
					del supply[flr]
					del costs[flr]

				if len(supply)==1:
					break

				if supply.get(er)!=None:
					step3=True
				else:
					step3= False

				continue
			else:
				max_supply = supply[slr]
				max_demand = demand[column_with_min_diff]

				for d in demand:
					max_supply -= res[slr][d]

				for s in supply:
					max_demand -= res[s][column_with_min_diff]

				max_demand+= res[flr][column_with_min_diff]
				max_demand+= res[slr][column_with_min_diff]

				max_supply+= res[slr][column_with_min_diff]

				# print(max_supply , max_demand)

				max_alloc = min(max_supply , max_demand)

				res[slr][column_with_min_diff] = max_alloc  #step 13

				res[flr][column_with_min_diff] += demand[column_with_min_diff] - max_alloc

				# print(res)
				demand[column_with_min_diff]=0
				tuslr=0
				for d in demand:
					tuslr += res[slr][d]

				if tuslr == supply[slr]:  #step 14
					# for d in demand:
					# 	demand[d] - res[flr][d]
					del supply[slr]
					del costs[slr]

				if supply.get(er)!=None:
					step3=True
				else:
					step3= False
				if len(supply)==1:
					break

				continue


		
		least_supply = 10000000
		second_least_supply= 1000000
		least_supply_row = "S"
		for s in supply:
			if supply[s]<least_supply:
				least_supply = supply[s]
				least_supply_row = s 
		for s in supply:
			if supply[s]<second_least_supply and s!=least_supply_row:
				second_least_supply = supply[s]

		# print(costs[flr][column_with_min_diff] , costs[slr][column_with_min_diff] , least_supply , second_least_supply)
		# print(res)

		# if costs[flr][column_with_min_diff]!=costs[slr][column_with_min_diff] and least_supply!=second_least_supply:  #step 7
			# print("here1" , status[slr])
		if True:
			if status[slr]=="ER": #step 8
				#step 9
				if True:
					# go to step 9
					# print(column_with_min_diff , slr)

					max_supply = supply[flr]
					max_demand = demand[column_with_min_diff]

					for d in demand:
						max_supply -= res[flr][d]

					for s in supply:
						max_demand -= res[s][column_with_min_diff]

					max_demand+= res[flr][column_with_min_diff]
					max_demand+= res[slr][column_with_min_diff]

					max_supply+= res[flr][column_with_min_diff]

					# print(max_supply , max_demand)

					max_alloc = min(max_supply , max_demand)
					max_alloc=max(max_alloc , 0 )
					res[flr][column_with_min_diff] = max_alloc  #step 13

					res[slr][column_with_min_diff] += demand[column_with_min_diff] - max_alloc

					# print(res)
					# demand[column_with_min_diff]=0
					tuflr=0
					for d in demand:
						tuflr += res[flr][d]

					if tuflr == supply[flr]:  #step 14
						for d in demand:
							demand[d]-=res[flr][d]

						del supply[flr]
						del costs[flr]

					if len(supply)==1:
						break

					if supply.get(er)!=None:
						step3=True
					else:
						step3= False

					continue

				pass
			else:
				# print("here2" , second_least_supply - least_supply , min_diff)

				# print((second_least_supply - least_supply) % min_diff==0)

				# if count==2:
				# 	exit()
				
				
				if min_diff!=0 and (second_least_supply - least_supply) % min_diff==0: # step 11
					# print("12")
					# print("This" , res)
					tcflr = 0
					tcslr = 0
					for d in demand:  #step 12
						tcflr += costs[flr][d]
						tcslr += costs[slr][d]
					# print(tcflr , tcslr)
					if tcflr>tcslr:
						max_supply = supply[flr]
						max_demand = demand[column_with_min_diff]

						for d in demand:
							max_supply -= res[flr][d]

						for s in supply:
							max_demand -= res[s][column_with_min_diff]

						max_demand+= res[flr][column_with_min_diff]
						max_demand+= res[slr][column_with_min_diff]

						max_supply+= res[flr][column_with_min_diff]

						# print(max_supply , max_demand)

						max_alloc = min(max_supply , max_demand)
						max_alloc=max(max_alloc , 0 )
						res[flr][column_with_min_diff] = max_alloc  #step 13

						res[slr][column_with_min_diff] += demand[column_with_min_diff] - max_alloc

						# print(res)
						# demand[column_with_min_diff]=0
						tuflr=0
						for d in demand:
							tuflr += res[flr][d]

						if tuflr == supply[flr]:  #step 14
							for d in demand:
								demand[d]-=res[flr][d]
							del supply[flr]
							del costs[flr]

						if supply.get(er)!=None:
							step3=True
						else:
							step3= False

						if len(supply)==1:
							break
						continue
						pass
					else:
						# print("13")
						# print(column_with_min_diff , slr)
						# print("comes here")
						# if count==2:
						# 	exit()
						max_supply = supply[slr]
						max_demand = demand[column_with_min_diff]

						for d in demand:
							max_supply -= res[slr][d]

						for s in supply:
							max_demand -= res[s][column_with_min_diff]

						max_demand+= res[flr][column_with_min_diff]
						max_demand+= res[slr][column_with_min_diff]

						max_supply+= res[slr][column_with_min_diff]

						# print(max_supply , max_demand)

						max_alloc = min(max_supply , max_demand)
						max_alloc=max(max_alloc , 0 )
						res[slr][column_with_min_diff] = max_alloc  #step 13

						res[flr][column_with_min_diff] += demand[column_with_min_diff] - max_alloc

						# print(res)
						# print("collections  " , column_with_min_diff)
						# demand[column_with_min_diff]=0
						tuslr=0
						for d in demand:
							tuslr += res[slr][d]

						if tuslr == supply[slr]:  #step 14
							for d in demand:
								demand[d]-=res[flr][d]
							del supply[slr]
							del costs[slr]

						if supply.get(er)!=None:
							step3=True
						else:
							step3= False
						if len(supply)==1:
							break

						continue

						# if count==2:
						# 	exit()
				else:
					# print("comes here now")

					# print(flr , slr)
					
					max_supply = supply[flr]
					max_demand = demand[column_with_min_diff]

					for d in demand:
						max_supply -= res[flr][d]

					for s in supply:
						max_demand -= res[s][column_with_min_diff]

					max_demand+= res[flr][column_with_min_diff]
					max_demand+= res[slr][column_with_min_diff]

					max_supply+= res[flr][column_with_min_diff]
					# max_supply+=res[slr][column_with_min_diff]


					# print(max_supply , max_demand)

					max_alloc = min(max_supply , max_demand)
					max_alloc=max(max_alloc , 0 )
					# print(max_alloc , flr , slr, column_with_min_diff)
					res[flr][column_with_min_diff] = max_alloc  #step 13

					res[slr][column_with_min_diff] += demand[column_with_min_diff] - max_alloc

					# print(res)
					# demand[column_with_min_diff]=0
					tuflr=0

					# print(res)

					
					for d in demand:
						tuflr += res[flr][d]

					if tuflr == supply[flr]:  #step 14
						for d in demand:
							demand[d]-=res[flr][d]
						del supply[flr]
						del costs[flr]

					if supply.get(er)!=None:
						step3=True
					else:
						step3= False

					if len(supply)==1:
						break
					# if count==2:
					# 	exit()
					continue



						# print(costs)
	# 	If FLCj is not equal to SLCj and LS is equal to SS, then go
	# to step 9.
		elif costs[flr][column_with_min_diff]!= costs[slr][column_with_min_diff] and least_supply==second_least_supply: #step 15
			#step 9
			max_supply = supply[flr]
			max_demand = demand[column_with_min_diff]

			for d in demand:
				max_supply -= res[flr][d]

			for s in supply:
				max_demand -= res[s][column_with_min_diff]

			max_demand+= res[flr][column_with_min_diff]
			max_demand+= res[slr][column_with_min_diff]

			max_supply+= res[flr][column_with_min_diff]

			# print(max_supply , max_demand)

			max_alloc = min(max_supply , max_demand)
			max_alloc=max(max_alloc , 0 )
			res[flr][column_with_min_diff] = max_alloc  #step 13

			res[slr][column_with_min_diff] += demand[column_with_min_diff] - max_alloc

			# print(res)
			# demand[column_with_min_diff]=0
			tuflr=0
			for d in demand:
				tuflr += res[flr][d]

			if tuflr == supply[flr]:  #step 14
				for d in demand:
					demand[d]-=res[flr][d]
				del supply[flr]
				del costs[flr]

			if supply.get(er)!=None:
				step3=True
			else:
				step3= False

			if len(supply)==1:
				break
			continue
			pass

		if len(supply)==1:  #step 18
			break

		# print(res)
		# break

	# print(res)
	# print("final" , res)

	cost = 0 

	for s in costs1.keys():
		for d in costs1[s].keys():
			if res[s][d]!=0:
				print( res[s][d]  , costs1[s][d])
			cost += res[s][d]*costs1[s][d]
	# print(alloc)

	print("final cost = ",cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('BCE-TCM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
