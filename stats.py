
import math
import numpy as np 


taskTimes =[84, 85, 86, 103, 111, 122, 180, 183, 235, 278]
print taskTimes

lnData=[]

for i in taskTimes:
	lnData.append(math.log(i))

# print lnData

print 'mean of ln data'
lnMean = np.mean(lnData)
print lnMean

print 'geometric mean'
geoMean = math.exp(lnMean)
print geoMean	

print 'median', np.median(taskTimes)
print 'mean', np.mean(taskTimes)

import matplotlib.pyplot as plt
plt.plot(taskTimes, 'b.')
plt.ylabel('Task Times')
plt.show()


# use scipy stats gmean


import scipy.stats as st

# prob to zscore
print st.norm.ppf(.95) 

# z-score to prob
print st.norm.cdf(1.64)
