import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
# 	D1	D2	D3	D4	Supply
# S1	19	30	50	12	7
# S2	70	30	40	60	10
# S3	40	10	60	20	18
# Demand	5	7	8	15	

# 	D1	D2	D3	Dummy	Supply
# S1	4	3	4	0	11
# S2	10	7	5	0	12
# S3	8	8	3	0	10
# S4	5	6	6	0	22
# Demand	16	10	14	15	

# costs = {"S1":{"D1":19 , "D2":30 , "D3": 50, "D4":12 },"S2":{"D1":70 , "D2": 30, "D3":40 , "D4":60 },
# "S3":{"D1": 40, "D2": 10 , "D3": 60 , "D4": 20}
# }

# demand = {"D1":5, "D2":7 , "D3":8 , "D4":15}
# supply = {"S1":7 , "S2":10 , "S3":18}

# costs = {"S1":{"D1":4 , "D2":3 , "D3": 4, "D4":0 },"S2":{"D1":10 , "D2": 7, "D3":5 , "D4":0 },
# "S3":{"D1": 8, "D2": 8 , "D3": 3 , "D4": 0}  , "S4":{"D1": 5, "D2": 6 , "D3": 6 , "D4": 0}
# }

# demand = {"D1":16 , "D2":10 , "D3":14 , "D4":15}

# supply = {"S1":11 , "S2":12 , "S3":10 , "S4":22}


cols = sorted(demand.keys())

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
		if sum(avr)!=0:
			avr = sum(avr)/len(avr)
			d[x] = pcaq/avr

		else: 
			d[x]= 0
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
		if sum(avr)!=0:
			avr = sum(avr)/len(avr)
			s[x] = pcaq/avr
		else:
			s[x]=0

	f = max(d, key=lambda n: d[n])
	t = max(s, key=lambda n: s[n])
	t, f = (f, g[f][0]) if d[f] >= s[t] else (g[t][0], t)
	v = min(supply[f], demand[t])
	print(d )
	print(s)
	print()
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
		cost += y * costs[g][n]
		# print ("  ",)
	# print(" ")

print(cost)