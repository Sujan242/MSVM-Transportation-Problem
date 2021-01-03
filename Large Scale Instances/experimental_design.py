# No. Transportation Problem :
# Parameter

# Number of
# Levels

# Values of the Parameter

# 1 Number of Supply Points ( m ) 4 10, 15, 20, 25
# 2 Number of Demand Points ( n ) 5 50, 100. 150, 200, 250
# 3 Cost Structure – Range( R ) 4 { 20, 100, 500, 1000 }
# 4 Degree of Imbalance ( K ) 4 { 1, 2, 5, 10 }
# Number of Problem Configurations 4 x 5 x 4 x 4 = 320
# Problem Instances per Configuration 5
# Total Problem Instances 320 x 5 = 1600
# Cost Structure (C ij ) : Uniform Distribution : U (C ij : Mean Cost - R/2 , Mean Cost + R/2)
# Where Mean Cost = 500
# Supply (S i ) : Uniform Distribution : U (S i : 0.75 x Mean Supply , 1.25 x Mean Supply),
# Where Mean Supply = [(K x n x Mean Demand) / m] and Mean Demand = 100
# Demand (D j ) : Uniform Distribution : U (D j : 75 , 125)
from random import uniform

costs_list=[]
demand_list=[]
supply_list=[]
for ns in [10,15,20,25]:
	for nd in [50,100,150,200,250]:
		for deg in [1,2,5,10]:
			for cost in [20,100,500,1000]:
				for instance in range(5):

					# ns=10
					x=500 - cost/2 
					y= 500 + cost/2 
					l=[[] for _ in range(ns)]
					for i in range(ns):
						for j in range(nd):
							l[i].append(int(uniform(x,y)))

					demand1= [ int(uniform(75,125)) for _ in range(nd)]
					mean_supply=int ((deg * (100*nd)*1.0) /ns) 
					supply1= [int(uniform(0.75 * mean_supply, 1.25* mean_supply)) for _ in range(ns)]
					ed=False
					es=False
					if sum(supply1)>sum(demand1):
						demand1.append(sum(supply1)-sum(demand1))
						ed=True
					elif sum(supply1)<sum(demand1):
						supply1.append(sum(demand1)-sum(supply1))
						es=True
					supply={}
					demand={}
					for i in range(len(demand1)):
						s="D"+str(i+1)
						demand[s]=demand1[i]

					for i in range(len(supply1)):
						s="S"+str(i+1)
						supply[s]=supply1[i]
					costs={}

					for i in range(ns):
						s="S"+str(i+1)
						dic={}
						for j in range(nd):
							s2="D"+str(j+1)
							dic[s2]=l[i][j] 
						if ed==True:
							dic["D" + str(nd+1)]=0
						costs[s]=dic
					if(es==True):
						s="S"+str(ns+1)
						dic={}
						for j in range(nd):
							s2="D"+str(j+1)
							dic[s2]=0 
						costs[s]=dic

					# print("costs = " , costs)
					# print("demand =", demand)
					# print("supply = ", supply)
					costs_list.append(costs)
					demand_list.append(demand)
					supply_list.append(supply)


print(len(costs_list))
import csv
from itertools import zip_longest
instance_number=range(1,1601)
d = [instance_number,costs_list,demand_list,supply_list]
export_data = zip_longest(*d, fillvalue = '')
with open('input.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs","Demand","Supply"))
      wr.writerows(export_data)
myfile.close()

				

