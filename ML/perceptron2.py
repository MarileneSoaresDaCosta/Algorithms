"""
Creating another example of data to test the perceptron algo

"""

import random
#get_ipython().magic(u'matplotlib inline')
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pylab
from pylab import rand  
from pylab import rand,plot,show,norm
import numpy as np


class Perceptron(object):
    """Perceptron classifier.
    Parameters
    ------------
    eta : float - NOT USED
        Learning rate (between 0.0 and 1.0)
        n_iter : int
        Passes over the training dataset.
    Attributes
    -----------
    w_ : 1d-array
        Weights after fitting.
    errors_ : list
        Number of misclassifications in every epoch.
    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    
    
    def fit(self, X, y):
        """Fit training data.
        Parameters
        ----------
            X : {array-like}, shape = [n_samples, n_features]
                Training vectors, where n_samples
                is the number of samples and
                n_features is the number of features.
            y : array-like, shape = [n_samples]
                Target values.
        Returns
        -------
               self : object
        """
        self.w_ = np.zeros(1 + X.shape[1])
        # print self.w_
        self.errors_ = []
           
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                #print "w ", self.w_, " target ", target, " self.predict(xi) ", self.predict(xi)
                update = self.eta * (target - self.predict(xi))
                #if update != 0.0:
                 #   print "update " , update, "xi ", xi, "w", self.w_
                self.w_[1:] += update * xi
                #print "update " , update, "xi ", xi, "w", self.w_, " update * xi ", update * xi
                self.w_[0] += update
                #print "update " , update, "xi ", xi, "w", self.w_
                errors += int(update != 0.0)
                #print errors
            self.errors_.append(errors)
        # print 'w vector', self.w_
        return self
        
        
    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X):
        """Return class label after unit step"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)
    

# create data    
n = 30
nx1 = rand(n)
max_x1 = 10 * (max(nx1))
nx2 = rand(n)
xr = zip(nx1*10, nx2*10)
#print xr  # X input in the perceptron implementation
x = np.array(xr)


b = []
r = []
yr = []

for pair in xr:
    #print pair[1]
    if pair[1] > (0.7*pair[0]+2):
        b.append(pair)
        yr.append(1)
    else:
        r.append(pair)
        yr.append(-1)

y = np.array(yr)
        
#print 'x', x

# print y

plt.figure(1)
plt.subplot(211)
plt.scatter([xa[0] for xa in b], [xa[1] for xa in b],color='green', marker='+', s=70)
plt.scatter([xa[0] for xa in r], [xa[1] for xa in r],color='red', marker='o')
# fig1 = plt.text(4, 11,'NOT guaranteed linear separation', horizontalalignment='center',verticalalignment='center', fontsize=15)
# plt.show()


# implementation

ppn = Perceptron(eta=0.01, n_iter=100)

ppn.fit(x, y)

plt.subplot(212)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs (n_iter)')
plt.ylabel('Number of misclassifications')
# plt.show()


print 'w vector', ppn.w_

# the plot line format is w1x1 + w2x2 + w0 = 0
x1list = []
x2list = []
# print 'x', x
# print int(max_x1)

for x1 in range(int(max_x1) + 1):
    x2 = ((-ppn.w_[1]*(x1) - ppn.w_[0])) / ppn.w_[2]
    x1list.append(x1)
    x2list.append(x2)

# print 'x1list', x1list
# print 'x2list', x2list

plt.subplot(211)
plt.plot(x1list, x2list)
plt.show()







# # plot of the separation line.
# # The separation line is orthogonal to w

# # checking the calculation of the norm
# print (ppn.w_[1]**2 +  ppn.w_[2]**2)**0.5

# ww = ppn.w_/wn
# print "ww", ww
# # ww1 = [ww[1],-ww[0]]
# # ww2 = [-ww[1],ww[0]]
# # plt.plot([ww1[0], ww2[0]],[ww1[1], ww2[1]],'--k')
# # plt.show()






