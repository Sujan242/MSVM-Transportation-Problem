import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
data= pd.read_csv('input.csv')

def standard_dev(l):
	mean = sum(l) / len(l)

	std = 0

	for x in l:
		std += (x-mean)*(x-mean)
	# print(mean , std)
	std/= len(l)
	std = math.sqrt(std)

	return std

output=[]
costs_list=[]
# [40 , 52 , 117 , 146 ,163 ]
for instance in range(640):
	print(instance+1)
	costs=ast.literal_eval(data['Costs'].iloc[instance])
	demand=ast.literal_eval(data['Demand'].iloc[instance])
	supply=ast.literal_eval(data['Supply'].iloc[instance])
	cols = sorted(demand.keys())
	costs1=copy.deepcopy(costs)
	# print(supply['S1'])
	# break
	# costs1=copy.deepcopy(costs)

	costs2=copy.deepcopy(costs)
	costs3=copy.deepcopy(costs)
	for i in supply:
	    mi=min(costs[i].values())
	    # print(costs[i])
	    # print(mi)
	    for j in costs2[i]:
	        costs2[i][j]-=mi
	# print(costs2)
	for i in demand :
	    mi=10000
	    for j in supply:
	        if costs[j][i]<mi :
	            mi=costs[j][i]
	    for j in supply:
	        costs3[j][i]=costs3[j][i]-mi 
	# print(costs3)

	for i in demand:
	    for j in supply:
	        costs[j][i]= costs2[j][i]+costs3[j][i]
	            

	res = dict((k, defaultdict(int)) for k in costs)
	g = {}
	for x in supply:
		# print(x)
		# print(costs[x])
		g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
	for x in demand:
		g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])
	 
	while g:
		d = {}
		# print(supply,demand)
		for x in demand:
			min_cost = costs[g[x][0]][x]
			feassible_quantity = min(demand[x] , supply[g[x][0]])
			min_cost_allocation = min_cost*feassible_quantity

			d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else (costs[g[x][0]][x])
			pcaq = d[x] * min_cost_allocation
			avr= []
			for y in supply:
				avr.append(costs[y][x])

			if sum(avr)!=0 and len(avr)>1:
				# avr = sum(avr)/len(avr)
				if standard_dev(avr)!=0:
					d[x] = pcaq / standard_dev(avr)
				else:
					d[x]=0
			else: 
				d[x]= 0

			# print(min_cost_allocation , pcaq , standard_dev(avr))
			# exit()
		s = {}
		for x in supply:
			min_cost = costs[x][g[x][0]]
			feassible_quantity = min(demand[g[x][0]] , supply[x])
			min_cost_allocation = min_cost*feassible_quantity

			s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]])  if len(g[x]) > 1 else costs[x][g[x][0]]
			pcaq = s[x]*min_cost_allocation
			avr= []
			for y in demand:
				avr.append(costs[x][y])
			if sum(avr)!=0 and len(avr)>1:
				# avr = sum(avr)/len(avr)
				if standard_dev(avr)!=0:
					s[x] = pcaq / standard_dev(avr)
				else:
					s[x]=0
			else:
				s[x]=0

		f = max(d, key=lambda n: d[n])
		t = max(s, key=lambda n: s[n])
		t, f = (f, g[f][0]) if d[f] >= s[t] else (g[t][0], t)
		v = min(supply[f], demand[t])
		# print(d )
		# print(s)
		# print()
		# # break
		# break
		# print(f,t)
		# print(v)
		res[f][t] += v
		demand[t] -= v
		
		if demand[t] == 0:
			for k, n in supply.items():
				if n != 0:
					g[k].remove(t)
			del g[t]
			del demand[t]
		supply[f] -= v
		if supply[f] == 0:
			for k, n in demand.items():
				if n != 0:
					g[k].remove(f)
			del g[f]
			del supply[f]
	 
	# print("G",g)
	cost = 0
	# cols = sorted(demand.keys())
	# print(costs)
	for g in sorted(costs):
		# print (g, " ",)
		# print("S")
		for n in cols:
			y = res[g][n]
			# print("YESS",y)
			if y != 0:
				pass
				# print (y,)
			cost += y * costs1[g][n]
			# print ("  ",)
		# print(" ")

	# print(cost)
	costs_list.append(cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,171)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('MSVM-3-TOCM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
