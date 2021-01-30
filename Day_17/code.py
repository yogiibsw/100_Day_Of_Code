
#Consider a random vector with shape (100,2) representing coordinates, find point by point distances

import numpy as np
import scipy
import scipy.spatial

Z = np.random.random((10,2))
X,Y = np.atleast_2d(Z[:,0], Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(D)


Z = np.random.random((10,2))
D = scipy.spatial.distance.cdist(Z,Z)
print(D)