import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
from math import sqrt
from statistics import stdev,mean
data= pd.read_csv('input.csv')

output=[]
costs_list=[]
for instance in range(171):
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
	ls=len(supply)
	while supply and demand:
		sd={}
		# print(demand,supply)
		for x in demand:
			# print(x)
			l=[]
			# print(len(supply))
			for y in supply:
				l.append(costs[y][x])
			# print(l)
			if len(supply)>1:

				sd[x]=mean(l)
			else:
				sd[x]=(list(supply.values()))[0]

		for y in supply :
			l=[]
			for x in demand:
				l.append(costs[y][x])
			if len(demand)>1:

				sd[y]=mean(l)
			else:
				sd[y]=(list(demand.values()))[0]
			# sd[y]=stdev(l)
		# print(sd)
		ma=max(sd.values())
		l=[]
		for ke in sd:
			if sd[ke]==ma:
				l.append(ke)
		ind=l[0]
		# # print(l)
		# mi=1000000
		# for ke in l:
		# 	if demand.get(ke)!=None:
		# 		for y in supply:
		# 			mi=min(mi,costs[y][ke])
		# 	else:
		# 		for x in demand:
		# 			mi=min(mi,costs[ke][x])
		# nl=[]
		# # print(mi)
		# flagg=0
		# if len(l)==1:
		# 	nl=l
		# 	flagg=1

		# for ke in l :
		# 	if flagg==1:
		# 		break
		# 	if demand.get(ke)!=None:
		# 		mi2=19000
		# 		for y in supply:
		# 			mi2=min(mi2,costs[y][ke])
		# 		if mi2==mi:
		# 			nl.append(ke)
		# 	else:
		# 		mi2=190000
		# 		for y in demand:
		# 			mi2=min(mi2,costs[ke][y])
		# 		if mi2==mi:
		# 			nl.append(ke)
		# # print(nl)
		# ind="D"
		# mi3=100000
		# flagg=0
		# if len(nl)==1:
		# 	ind=nl[0]
		# 	flagg=1

		# for ke in nl :
		# 	if flagg==1:
		# 		break
		# 	if demand.get(ke)!=None:

		# 		mi2=10000
		# 		for y in supply:
		# 			if costs[y][ke]<mi2:
		# 				mi2=costs[y][ke]
		# 		if mi2<mi3:
		# 			mi3=mi2
		# 			ind=ke
		# 	else:
		# 		mi2=10000
		# 		for y in demand:
		# 			if costs[ke][y]<mi2:
		# 				mi2=costs[ke][y]
		# 		if mi2<mi3:
		# 			mi3=mi2
		# 			ind=ke
		# print(ind)
		if demand.get(ind)!=None:
			mi=10000
			mind="S"
			for y in supply:
				if costs[y][ind]<mi:
					mi=costs[y][ind]
					mind=y
			v=min(supply[mind],demand[ind])
			supply[mind]-=v
			demand[ind]-=v
			res[mind][ind]+=v
			if supply[mind]==0:
				del supply[mind]
			if demand[ind]==0:
				del demand[ind]
		else:
			mi=10000
			mind="S"
			# print(ind)
			for y in demand:
				# print(ind,y)
				if costs[ind][y]<mi:
					mi=costs[ind][y]
					mind=y
			v=min(supply[ind],demand[mind])
			supply[ind]-=v
			demand[mind]-=v
			res[ind][mind]+=v
			if supply[ind]==0:
				del supply[ind]
			if demand[mind]==0:
				del demand[mind]

		# break


	# print(demand,supply)

	cost = 0
	for g in sorted(costs1):
		# print (g, "\t",)
		for n in cols:
			y = res[g][n]
			if y != 0:
				pass
				# print (y,)
			cost += y * costs1[g][n]
			# print ("\t",)
		# print()
	# print ("\n\nTotal Cost = ", cost)
	
	costs_list.append(cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('Geometric_mean-TOM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
