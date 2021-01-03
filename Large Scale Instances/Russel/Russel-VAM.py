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

	costs2=copy.deepcopy(costs)
	costs3=copy.deepcopy(costs)
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
	#         costs[j][i]= costs2[j][i]+costs3[j][i]
	            

	res = dict((k, defaultdict(int)) for k in costs)
	g = {}
	for x in supply:
		g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g], reverse=True)
	for x in demand:
		g[x] = sorted(costs.keys(), key=lambda g: costs[g][x] , reverse=True)
	g1={}
	for x in supply:
		g1[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
	for x in demand:
		g1[x] = sorted(costs.keys(), key=lambda g: costs[g][x] )

	# print(costs1)
	flag=0
	while g:
	   
		d = {}
		# print(demand,supply)
		for x in demand:
			d[x] = (costs[g1[x][0]][x]*costs[g[x][0]][x]) 
		# s = {}
		for x in supply:
			d[x] = (costs[x][g1[x][0]]*costs[x][g[x][0]]) 

		# print(d)
		f = max(d, key=lambda n: d[n])
		# print(f)
		
		# break
		t="D"
		if demand.get(f)!=None:

			t, f= (f, g1[f][0] )
		else:
			t,f = (g1[f][0], f)
		v = min(supply[f], demand[t])        
		res[f][t] += v
		demand[t] -= v
		
		if demand[t] == 0:
			for k, n in supply.items():
				if n != 0:
					g[k].remove(t)
					g1[k].remove(t)
			del g[t]
			del g1[t]
			del demand[t]
		supply[f] -= v
		if supply[f] == 0:
			for k, n in demand.items():
				if n != 0:
					g[k].remove(f)
					g1[k].remove(f)
			del g[f]
			del g1[f]
			del supply[f]

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
with open('Russel-VAM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
