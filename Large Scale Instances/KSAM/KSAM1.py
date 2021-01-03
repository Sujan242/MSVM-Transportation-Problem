import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
data= pd.read_csv('input.csv')

output=[]
costs_list=[]
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
	ma=0 
	
	            

	res = dict((k, defaultdict(int)) for k in costs)
	rij={}
	for x in supply:
		dd={}
		for y in demand:
			dd[y]=0
		rij[x]=dd 

	for x in supply:
		for y in demand:
			rij[x][y]= supply[x]/demand[y] 
	# print(rij)
	for x in supply:
		for y in demand:
			rij[x][y]*=costs[x][y]



	while supply or demand:
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
	# print ("\n\nTotal Cost = ", cost)
	
	costs_list.append(cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('KSAM1.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
