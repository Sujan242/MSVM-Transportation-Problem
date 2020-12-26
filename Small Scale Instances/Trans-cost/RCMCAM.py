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
    
	# print(supply['S1'])
	# break
	            

	res = dict((k, defaultdict(int)) for k in costs)
	g = {}
	for x in supply:
		# print(x)
		# print(costs[x])
		g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
	for x in demand:
	    g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])
	 
	while g and supply:
	    d = {}
	    # print(supply,demand)
	    f_quant={}
	    for x in demand:
	        d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else (costs[g[x][0]][x])
	        
	        f_quant[x]=min(demand[x],supply[g[x][0]]) * costs[g[x][0]][x]
	    s = {}
	    for x in supply:
	        s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]])  if len(g[x]) > 1 else costs[x][g[x][0]]
	        
	        f_quant[x]=min(supply[x], demand[g[x][0]]) * costs[x][g[x][0]]
	    # print(f_quant)
	    t,f=0,0
	    # break
	    fm = max(f_quant,key=lambda n: f_quant[n])
	    if demand.get(fm)!=None:
	    	t,f = fm , g[fm][0]
	    else:
	    	t,f = g[fm][0],fm
	    # print(t,f)
	    # break
	    # t, f = (f, g[f][0]) if d[f] >= s[t] else (g[t][0], t)
	    v = min(supply[f], demand[t])
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
	print(supply,demand)
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
	# print(cost)
	costs_list.append(cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('RCMCAM-VAM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
