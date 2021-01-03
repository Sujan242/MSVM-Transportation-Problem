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
	
	            

	res = dict((k, defaultdict(int)) for k in costs)
	ld=len(demand)

	flag=0
	flagd=0
	sddd=""
	if ld%10==1:
		s="D"+ str(ld)
		sddd=s
		flagd=demand[s]
		del demand[s]
		ld=ld-1
		flag=1

	g={}
	for x in supply:
	    g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
	for x in demand:
	    g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])

	num=0
	while num<ld:
		num=num+1
		d={}
		for x in demand:
			d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else costs[g[x][0]][x]

		k=max(demand.items(), key=lambda x: x[1])
		# print(d)
		# print(k)
		sd=[]
		for x in demand:
			if demand[x]==k[1]:
				sd.append(x)
		ma=-1
		for x in sd :
			if d[x]>ma :
				ma=d[x]
		nd=[]
		for x in sd:
			if d[x]==ma :
				nd.append(x)
		dem="D"
		mi=1000
		for x in nd :
			for y in supply:
				if (costs[y][x] /(1.0* demand[x])) <mi :
					mi= (costs[y][x] /(1.0* demand[x]))
					dem = x 
	    
		# print(dem)
		while(demand[dem]>0):
			mi=100000
			mind="D"
	        
			for y in supply :
				if costs[y][dem]<mi:
					mi=costs[y][dem]
					mind=y
			v= min(supply[mind],demand[dem])
			res[mind][dem]+=v
			supply[mind]-=v 
			demand[dem]-=v
			if supply[mind] == 0:
			    for k, n in demand.items():
			        if n != 0:
			            g[k].remove(mind)
			    del g[mind]
			    del supply[mind]
		for k, n in supply.items():
		    if n != 0:
		        g[k].remove(dem)
		del g[dem]
		del demand[dem]

	if flag==1:

		while flagd >0 :
			mi=100000
			mind="D"
			
			for y in supply :
				if costs[y][sddd]<mi:
					mi=costs[y][sddd]
					mind=y
			v= min(supply[mind],flagd)
			res[mind][sddd]+=v
			supply[mind]-=v 
			flagd-=v
			if supply[mind] == 0:
			    for k, n in demand.items():
			        if n != 0:
			            g[k].remove(mind)
			    del g[mind]
			    del supply[mind]




	# print(supply)	
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
	# print ("\n\nTotal Cost = ", cost)
	
	costs_list.append(cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('Max-demand-VOM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
