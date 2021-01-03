import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
from math import sqrt
from statistics import stdev 
# costs  = {'S1': {'D1': 3, 'D2': 4, 'D3': 6} , 'S2':{'D1': 7, 'D2': 3, 'D3': 8} , 'S3':{'D1': 6, 'D2': 4, 'D3': 5}, 'S4':{'D1': 7, 'D2': 5, 'D3': 2}}
costs = {'S1':{'D1': 8, 'D2': 6, 'D3': 10 , 'D4':9},'S2':{'D1': 9, 'D2': 12, 'D3': 13 , 'D4':7},'S3':{'D1': 14, 'D2': 9, 'D3': 16 , 'D4':5}}
demand = {'D1': 45, 'D2': 20, 'D3':30, 'D4':30}
cols = sorted(demand.keys())
supply ={'S1': 35, 'S2': 50, 'S3': 40}
res = dict((k, defaultdict(int)) for k in costs)
g = {}
for x in supply:
	g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
for x in demand:
	g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])
# print(costs1)
flag=0
while demand:
	l=[]
	# print(demand)
	for x in demand:

		# print(demand[x],supply[g[x][0]])
		if demand[x]> supply[g[x][0]]:
			l.append(x)
			if len(l)==2:
				break
	# break
	mi=100000
	dem="D"
	if l:

		print(l)
	if len(l)==0:
		for x in demand:
			print(x, g[x][0])
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
		print(g[x][0])
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





print(res)
print(demand,supply)	
 
# print(costs1)
cost = 0
for g in sorted(costs):
	# print (g, " ",)
	for n in cols:
		y = res[g][n]
		if y != 0:
			pass
			# print (y,)
		print(costs[g][n]  ,y)
		cost += y * costs[g][n]
		# print ("  ",)
	# print(" ")
print ("Total Cost = ", cost)