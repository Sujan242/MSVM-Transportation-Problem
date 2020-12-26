import pandas as pd 
data=pd.read_excel('MSV-Results.xlsx',header=None)

num=[[0 for _ in range(6)] for _ in range(5)]

ls=[[],[]]
for i in range(2,145):

	print(data.iloc[i])
	l = data.iloc[i]
	# l = [:-1]
	optimal = l[len(l)-1]
	# exit()
	for lcv in range(1, 7):
		v= (l[lcv] - optimal)/optimal
		v*=100
		# if m==2 or m==3:
		# 	if abs(v)<=0.000006:
		# 		ls[m-2].append(i)



		m=lcv-1
		if abs(v-0)<=0.000006 :
			num[0][m]+=1
		if v<=0.5:
			num[1][m]+=1
		if v<=1:
			num[2][m]+=1
		if v<=2:
			num[3][m]+=1
		if v<=3:
			num[4][m]+=1


# print(len(ls[0]), len(ls[1]))
# print(ls)
import csv
from itertools import zip_longest
d = num
# d=list(map(list, zip(*d)))
# d=list(map(list, zip(*d)))
export_data = zip_longest(*d, fillvalue = '')
with open('Evaluation_with_optimal.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      #wr.writerow(("SIZE", "ERT","LPT ","EDD","ODD", "FDD","CGH_LST","CI","SIZE-ANN","ERT-ANN","LPT-ANN","EDD-ANN","ODD-ANN","FDD-ANN","ANN-LST",))
      wr.writerows(export_data)
myfile.close()


