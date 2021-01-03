import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
from math import sqrt
from statistics import stdev 
costs  = {"S1":{"D1":73,"D2":40,"D3":9,"D4":79 ,"D5":20,},"S2":{"D1":62,"D2":93,"D3":96,"D4":8 ,"D5":13,},"S3":{"D1":96,"D2":65,"D3":80,"D4":30 ,"D5":65,},"S4":{"D1":57,"D2":58,"D3":29,"D4":12 ,"D5":87,},"S5":{"D1":56,"D2":23,"D3":87,"D4":18 ,"D5":12,}}

demand = {"D1":6,"D2":8,"D3":10,"D4":4 ,"D5":4,}
cols = sorted(demand.keys())
supply ={"S1":8,"S2":7,"S3":9,"S4":3,"S5":5}
res = dict((k, defaultdict(int)) for k in costs)

rij={}
for x in supply:
	dd={}
	for y in demand:
		dd[y]=0
	rij[x]=dd 

for x in supply:
	for y in demand:
		rij[x][y]= demand[y] /supply[x]
# print(rij)
for x in supply:
	for y in demand:
		rij[x][y]*=costs[x][y]

for i in rij:
	print(rij[i])

while supply and demand:
	mi=10000000000000
	l=[]
	for x in supply:
		for y in demand:
			if rij[x][y]<mi:
				mi=rij[x][y]
				l=[x,y]

	sup=l[0]
	dem=l[1]
	v=min(supply[sup],demand[dem])
	demand[dem]-=v
	supply[sup]-=v
	res[sup][dem]+=v
	if supply[sup]==0:
		del supply[sup]
	if demand[dem]==0:
		del demand[dem]

	


print(demand,supply)

cost = 0
for g in sorted(costs):
	# print (g, "\t",)
	for n in cols:
		y = res[g][n]
		if y != 0:
			pass
			# print (y,)
		cost += y * costs[g][n]
		# print ("\t",)
	# print()
print ("\n\nTotal Cost = ", cost)
