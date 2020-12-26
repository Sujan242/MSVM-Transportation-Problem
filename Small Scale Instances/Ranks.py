import pandas as pd
import ast
data=pd.read_excel('MSV-Results.xlsx')
import scipy.stats as ss
ol=[]

for i in range(1,145):
	# print(data.iloc[i,2:].values.tolist())
	l= data.iloc[i,1:-1].values.tolist()
	print(l)
	# exit()
	print(len(l))
	# break
	o=[(sorted(l).index(x)+1) for x in l]
	# print(o)
	ol.append(o)
	# break

# print(ol)
print(len(ol[0]))

import csv
from itertools import zip_longest


d = ol

d=list(map(list, zip(*d)))
export_data = zip_longest(*d, fillvalue = '')
with open('Ranks.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      #wr.writerow(("SIZE", "ERT","LPT ","EDD","ODD", "FDD","CGH_LST","CI","SIZE-ANN","ERT-ANN","LPT-ANN","EDD-ANN","ODD-ANN","FDD-ANN","ANN-LST",))
      wr.writerows(export_data)
myfile.close()