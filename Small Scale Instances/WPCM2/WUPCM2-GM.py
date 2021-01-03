import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
data= pd.read_csv('input.csv')

output=[]
costs_list=[]
for instance in range(170):
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
		g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
	for x in demand:
		g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])
	# print(costs1)
	flag=0
	while g:
	   
		d = {}
		# print(demand,supply)

		for x in demand:
			d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else (costs[g[x][0]][x])
		s = {}
		for x in supply:
			s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]]) if len(g[x]) > 1 else costs[x][g[x][0]]
		
		# t1, f1 , maxp= (f, g[f][0] , d[f]) if d[f] > s[t] else (g[t][0], t , s[t])
		# v = min(supply[f1], demand[t1])

		# print(d,s)
		tfin="S"
		fin="D"
		ma=-1
		for x in demand:
			mi=100000
			mind="S"
			for y in supply:
				if costs[y][x] < mi:
					mi=costs[y][x]
					mind=y
			term = d[x] * mi
			avr= []
			for y in supply:
				avr.append(costs[y][x])
			if sum(avr)!=0:
				avr = sum(avr)/len(avr)
				term/=avr

			else: 
				# d[x]= 0
				term=0
			# print(term)
			if term>ma:
				tfin , fin = x , g[x][0]
				ma=term
		for y in supply :
			mi=100000
			mind="D"
			for x in demand:
				if costs[y][x]<mi :
					mi=costs[y][x] 
					mind=x
			term=s[y]* mi
			avr= []
			for y in supply:
				avr.append(costs[y][x])
			if sum(avr)!=0:
				avr = sum(avr)/len(avr)
				term/=avr

			else: 
				# d[x]= 0
				term=0
			if term>ma :
				tfin,fin = g[y][0] , y 
				ma=term

		t,f=tfin,fin
		# print(t,f)
		v = min(supply[f], demand[t])        
		res[f][t] += v
		demand[t] -= v
		# print(ma , f , t)
		# print(f"Allocate {v} units from {f} to {t}")
		
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
		# print()
		
	# print(supply,demand)
	# break
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
with open('WPCM2-GM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
