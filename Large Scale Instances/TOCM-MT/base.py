import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
from math import sqrt
from statistics import stdev 
costs  = {"S1":{"D1":9, "D2":42 , "D3": 50, "D4": 0} , "S2":{"D1":91, "D2":22 , "D3": 10, "D4": 80} ,"S3":{"D1":53, "D2":0 , "D3": 92, "D4": 22}  }

demand = {"D1":5, "D2":8 , "D3": 7, "D4": 14}
supply={"S1":7, "S2":9 , "S3": 18}
cols = sorted(demand.keys())
# supply =
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
while supply and demand:
   
	d = {}
	# print(demand,supply)
	
	s = {}
	for x in supply:
		s[x] = 0
		for y in demand:
			s[x]=s[x] + costs[x][y]- costs[x][g[x][0]]

	mp = max(list(s.values()))
	mi=1000000
	l=[]
	for x in supply :
		if s[x]==mp:
			l.append(x)
			if costs[x][g[x][0]]<mi:
				mi=costs[x][g[x][0]]
	sup="S"
	ma=0
	# print(demand)
	for x in l :
		print(g[x][0])
		if costs[x][g[x][0]]==mi and demand[g[x][0]]>=ma:
			sup=x 
	# print(costs[sup][g[sup][0]], len(supply))
	if costs[sup][g[sup][0]]!=0 or len(supply)==1:
		# print("here")
		v=min(supply[sup],demand[g[sup][0]])
		# print(sup,demand,v)
		demand[g[sup][0]]-=v
		supply[sup]-=v 
		res[sup][g[sup][0]]+=v 
		dem = g[sup][0]
		print(sup,dem,v)
		if demand[dem]==0:
			for k, n in supply.items():
			    if n != 0:
			        g[k].remove(dem)
			del g[dem]
			del demand[dem]
		if supply[sup]==0:
			for k, n in demand.items():
			    if n != 0:
			        g[k].remove(sup)
			del g[sup]
			del supply[sup]

	else :
		mind="S"
		ma=-1
		# print(sup)
		for x in supply :
			if s[x]>ma and x!=sup :
				ma=s[x]
				mind=x
		gv1=0
		# print(mind,"this")
		for y in demand:
			if costs[sup][y] > costs[mind][y]:
				gv1+=1 
			else:
				gv1-=1
		if gv1>=0 :
			v=min(supply[sup],demand[g[sup][0]])
			# print(sup,demand,v)
			demand[g[sup][0]]-=v
			supply[sup]-=v 
			res[sup][g[sup][0]]+=v 
			dem=g[sup][0]
			print(sup,dem,v)
			if demand[dem]==0:
				for k, n in supply.items():
				    if n != 0:
				        g[k].remove(dem)
				del g[dem]
				del demand[dem]
			if supply[sup]==0:
				for k, n in demand.items():
				    if n != 0:
				        g[k].remove(sup)
				del g[sup]
				del supply[sup]
		else :
			sup=mind 
			v=min(supply[sup],demand[g[sup][0]])
			
			demand[g[sup][0]]-=v
			supply[sup]-=v 
			res[sup][g[sup][0]]+=v 
			dem=g[sup][0]
			print(sup,dem,v)
			if demand[dem]==0:
				for k, n in supply.items():
				    if n != 0:
				        g[k].remove(dem)
				del g[dem]
				del demand[dem]
			if supply[sup]==0:
				for k, n in demand.items():
				    if n != 0:
				        g[k].remove(sup)
				del g[sup]
				del supply[sup]
	# break

# print(demand,supply)	

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
print ("Total Cost = ", cost)