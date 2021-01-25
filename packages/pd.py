import pandas as pd
import numpy as np

def bubble_sort(alist):
	lenlist = len(alist)
	for i in range(0, lenlist - 1):
		for j in range(lenlist - 1, i, -1):
			if alist[j] < alist[j-1]:
				temp 		= alist[j]
				alist[j] 	= alist[j-1]
				alist[j-1] 	= temp
	return alist

alist = [121, 1541, 1212, 121, 155, 4545, 12, 1, 15, 2155, 155, 5448, 454]
alist = bubble_sort(alist)
nplist = np.array(alist)
series = pd.Series(nplist)
print(series)