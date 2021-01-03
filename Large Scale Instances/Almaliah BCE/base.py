# 	D1	D2	D3	D4	Supply
# S1	10	2	20	11	15
# S2	12	7	9	20	25
# S3	4	14	16	18	10
# Demand	5	15	15	15	
import copy
# costs = {"S1":{"D1":10 , "D2":2 , "D3":20 , "D4":11} , "S2":{"D1":12 , "D2":7 , "D3":9 , "D4":20} ,
#  "S3":{"D1":4 , "D2":14 , "D3":16 , "D4":18}}

# costs1=copy.deepcopy(costs)

# supply = {"S1":15 , "S2":25 , "S3":10}
# demand = {"D1":5, "D2":15 , "D3": 15 , "D4" : 15}

costs = {"S1":{"D1":3 , "D2":6 , "D3":3 , "D4":4} , "S2":{"D1":6 , "D2":5 , "D3":11 , "D4":15}}
costs1=copy.deepcopy(costs)
supply = {"S1":80 , "S2":90}
demand = {"D1":70, "D2":5 , "D3": 35 , "D4" : 60}

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
	# print(supply)
	alloc = res
	# print(res)
	
	if step3==False:
		res = alloc
		er="S"
		for s in supply:  #step 3
			alc = 0
			for d in demand:
				alc += alloc[s][d]
			if alc>supply[s]:
				# print(alc)
				status[s]="ER"
				er=s 
	# print(er)
	# status[er] = "ER"
	flr="S"
	slr="S"
	min_diff=100000000000
	column_with_min_diff="D"
	for d in demand:  #step 5
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

			res[slr][column_with_min_diff] = demand[column_with_min_diff] - max_alloc

			# print(res)
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

			res[flr][column_with_min_diff] = demand[column_with_min_diff] - max_alloc

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

	if costs[flr][column_with_min_diff]!=costs[slr][column_with_min_diff] and least_supply!=second_least_supply:  #step 7
		# print("here1" , status[slr])
		
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

				res[slr][column_with_min_diff] = demand[column_with_min_diff] - max_alloc

				# print(res)
				demand[column_with_min_diff]=0
				tuflr=0
				for d in demand:
					tuflr += res[flr][d]

				if tuflr == supply[flr]:  #step 14

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
			
			
			if (second_least_supply - least_supply) % min_diff==0: # step 11
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

					res[slr][column_with_min_diff] = demand[column_with_min_diff] - max_alloc

					# print(res)
					demand[column_with_min_diff]=0
					tuflr=0
					for d in demand:
						tuflr += res[flr][d]

					if tuflr == supply[flr]:  #step 14
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

					res[flr][column_with_min_diff] = demand[column_with_min_diff] - max_alloc

					# print(res)
					demand[column_with_min_diff]=0
					tuslr=0
					for d in demand:
						tuslr += res[slr][d]

					if tuslr == supply[slr]:  #step 14
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

				res[slr][column_with_min_diff] = demand[column_with_min_diff] - max_alloc

				# print(res)
				demand[column_with_min_diff]=0
				tuflr=0

				# print(res)

				
				for d in demand:
					tuflr += res[flr][d]

				if tuflr == supply[flr]:  #step 14
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

		res[slr][column_with_min_diff] = demand[column_with_min_diff] - max_alloc

		# print(res)
		demand[column_with_min_diff]=0
		tuflr=0
		for d in demand:
			tuflr += res[flr][d]

		if tuflr == supply[flr]:  #step 14
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
		# if res[s][d]!=0:
		# 	print( res[s][d]  , costs1[s][d])
		cost += res[s][d]*costs1[s][d]

print(cost)