"""
Creating Perceptron algorithms
"""


# coding: utf-8

# In[1]:

import random
get_ipython().magic(u'matplotlib inline')
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pylab

"""
Creating data that is guaranteed to be linearly separable
"""

# In[2]:

#randx = [[random.uniform(0,10),random.uniform(0,10)] for x in nx]
#npx = np.array(origx)
#print randx

n = 20
from pylab import rand      # rand(d0, d1, ..., dn) Random values in a given shape. 
                            # Create an array of the given shape and propagate it with
                            # random samples from a uniform distribution over ``[0, 1)``.


xb = (rand(n)*2-1)/2-0.5
yb = (rand(n)*2-1)/2+0.5
xr = (rand(n)*2-1)/2+0.5
yr = (rand(n)*2-1)/2-0.5

inputs = []
#print xb
for i in range(len(xb)):
    inputs.append([xb[i],yb[i],1])
    inputs.append([xr[i],yr[i],-1])

#print inputs

Xinputs = []
Yinputs = []

for i in range(len(inputs)):
    Xinputs.append([inputs[i][0],inputs[i][1]])
    Yinputs.append(inputs[i][2])
    
#print 'x  ', Xinputs
#print 
#print
#print 'y   ',Yinputs




b = []
r = []

for xi in inputs:
    if xi[2] > 0:
        b.append(xi)
    else:
        r.append(xi)

plt.scatter([x[0] for x in b], [x[1] for x in b],color='blue', marker='+', s=70)
plt.scatter([x[0] for x in r], [x[1] for x in r],color='red', marker='o')

plt.text(-1.0, 1.2,'guaranteed linear separation',fontsize=15)

plt.show()
#print b




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
        return self
        
        
    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X):
        """Return class label after unit step"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)
    


# In[8]:
"""
using the example from the Book Python Machine Learning 

"""

import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df.tail()


# In[9]:

df[0].max()


# In[10]:

"""
extract the first 100 class labels that correspond to the 50 Iris-Setosa and 50 Iris-Versicolor flowers, 
and convert the class labels into the two integer class labels 1 (Versicolor) and -1 (Setosa) 
that we assign to a vector y where the values method of a pandas DataFrame yields 
the corresponding NumPy representation. 
"""

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

"""
Similarly, we extract the first feature column (sepal length) 
and the third feature column (petal length) 
of those 100 training samples and assign them to a feature matrix X, 
which we can visualize via a two-dimensional scatter plot:
"""
X = df.iloc[0:100, [0, 2]].values
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')

plt.show()


# In[11]:

"""
Now we train our perceptron algorithm on the Iris data subset that we just extracted. 
Also, we will plot the misclassification error for each epoch to check if the algorithm converged and
found a decision boundary that separates the two Iris  ower classes:
"""
ppn = Perceptron(eta=0.01, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()


# In[12]:

from matplotlib.colors import ListedColormap
def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                     np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    #print Z
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                alpha=0.8, c=cmap(idx),
                marker=markers[idx], label=cl)
        
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()


# In[13]:

# testing how to add a line


from pylab import rand,plot,show,norm

# plot of the separation line.
# The separation line is orthogonal to w
n = norm(ppn.w_)
print n

# checking the calculation of the norm
#print (perceptron.w[0]**2 +  perceptron.w[1]**2)**0.5

ww = ppn.w_/n
print "ww", ww
ww1 = [ww[1],-ww[0]]
ww2 = [-ww[1],ww[0]]
plt.plot([ww1[0], ww2[0]],[ww1[1], ww2[1]],'--k')
plt.show()


# In[14]:

# printing the dataset and the separation line

X = df.iloc[0:100, [0, 2]].values
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')

x1a = []
x2a = []

for x1 in range(4, 9):
    x2 = ((-ww[1]*x1)-ww[0])/ww[2]
    x1a.append(x1)
    x2a.append(x2)

x1,x2,X,y = plt.axis()

plt.axis((x1,x2,0,6))

# print x1a, x2a
plt.plot(x1a, x2a,'--k')

#%pylab inline
pylab.rcParams['figure.figsize'] = (10, 6)

plt.show()






