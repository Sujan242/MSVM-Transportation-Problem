import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
data= pd.read_csv('input.csv')

output=[]
costs_list=[]
for instance in range(1600):
	print(instance+1)
	costs=ast.literal_eval(data['Costs'].iloc[instance])
	demand=ast.literal_eval(data['Demand'].iloc[instance])
	supply=ast.literal_eval(data['Supply'].iloc[instance])
	cols = sorted(demand.keys())
	costs1=copy.deepcopy(costs)
	# print(supply['S1'])
	# break
	# costs1=copy.deepcopy(costs)

	# costs2=copy.deepcopy(costs)
	# costs3=copy.deepcopy(costs)
	# for i in supply:
	#     mi=min(costs[i].values())
	#     # print(costs[i])
	#     # print(mi)
	#     for j in costs2[i]:
	#         costs2[i][j]-=mi
	# # print(costs2)
	# for i in demand :
	#     mi=10000
	#     for j in supply:
	#         if costs[j][i]<mi :
	#             mi=costs[j][i]
	#     for j in supply:
	#         costs3[j][i]=costs3[j][i]-mi 
	# # print(costs3)

	# for i in demand:
	#     for j in supply:
	#         costs[j][i]= max(costs2[j][i],costs3[j][i])
	            

	res = dict((k, defaultdict(int)) for k in costs)
	g = {}
	for x in supply:
	    g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
	for x in demand:
	    g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])
	# print(costs1)
	flag=0
	while g:
		l=[]
		for x in demand:

			# print(demand[x],supply[g[x][0]])
			if demand[x]> supply[g[x][0]]:
				l.append(x)
				if len(l)==2:
					break
		# break
		mi=100000
		dem="D"
		# print(l)
		if len(l)==0:
			for x in demand:
				t=g[x][0]
				res[t][x]+=demand[x]
				supply[t]-=demand[x]
				demand[x]=0
				if supply[t]==0:
					if supply[t] == 0:
						for k, n in demand.items():
							if n != 0:
								g[k].remove(t)
					del g[t]
					del supply[t]
				for k, n in supply.items():
					if n != 0:
						g[k].remove(x)
				del g[x]
				del demand[x]
				break
			continue
		for x in l:

			diff = costs[g[x][1]][x]-costs[g[x][0]][x] if len(g[x])>1 else costs[g[x][0]]
			if diff < mi:
				mi=diff
				dem=x
		x=dem 

		# print(x,mi)
		# break
		
		while(demand[x]>0):

			v=min(demand[x],supply[g[x][0]])
			demand[x]-=v
			supply[g[x][0]]-=v
			res[g[x][0]][x]+=v
			t=g[x][0]
			# print(t)

			if supply[t]==0:
				if supply[t] == 0:
					for k, n in demand.items():
						if n != 0:
							g[k].remove(t)
				del g[t]
				del supply[t]
		for k, n in supply.items():
			if n != 0:
					g[k].remove(x)
		del g[x]
		del demand[x]

	   
	# for x in demand:

	# 	t= g[x][0]
	# 	if demand[x]> supply[t]:
	# 		print("Help")
	# 	res[t][x]+= demand[x] 
	# 	demand[x]=0
	# 	supply[t]-= demand[x]
		
	# 	if supply[t]==0:
	# 		if supply[t] == 0:
	# 			for k, n in demand.items():
	# 				if n != 0:
	# 					g[k].remove(t)
	# 		del g[t]
	# 		del supply[t]
	# 	for k, n in supply.items():
	# 		if n != 0:
	# 			g[k].remove(x)
	# 	del g[x]





	print(demand,supply)	
	 
	# print(costs1)
	cost = 0
	for g in sorted(costs1):
		# print (g, " ",)
		for n in cols:
			y = res[g][n]
			if y != 0:
				pass
				# print (y,)
			cost += y * costs1[g][n]
			# print ("  ",)
		# print(" ")
	# print ("Total Cost = ", cost)
	
	costs_list.append(cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('JHM-TCM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
