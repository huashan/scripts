#!/usr/bin/python
#input:

#=====================================================
# purpose: logistic regression 
import numpy as np
import scipy as sp
import scipy.optimize

import matplotlib as mpl
import os

# prepare the data
data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
vY = data[:, 0]
mX = data[:, 1:]
# mX = (mX - np.mean(mX))/np.std(mX)  # standardize the data; if required

intercept = np.ones(mX.shape[0]).reshape(mX.shape[0], 1)
mX = np.concatenate((intercept, mX), axis = 1)
iK = mX.shape[1]
iN = mX.shape[0]

# logistic transformation
def logit(mX, vBeta):
    return((np.exp(np.dot(mX, vBeta))/(1.0 + np.exp(np.dot(mX, vBeta)))))

# test function call
vBeta0 = np.array([-.10296645, -.0332327, -.01209484, .44626211, .92554137, .53973828, 
    1.7993371, .7148045  ])
logit(mX, vBeta0)

# cost function
def logLikelihoodLogit(vBeta, mX, vY):
    return(-(np.sum(vY*np.log(logit(mX, vBeta)) + (1-vY)*(np.log(1-logit(mX, vBeta))))))
logLikelihoodLogit(vBeta0, mX, vY) # test function call

# different parametrization of the cost function
def logLikelihoodLogitVerbose(vBeta, mX, vY):
    return(-(np.sum(vY*(np.dot(mX, vBeta) - np.log((1.0 + np.exp(np.dot(mX, vBeta))))) +
                    (1-vY)*(-np.log((1.0 + np.exp(np.dot(mX, vBeta))))))))
logLikelihoodLogitVerbose(vBeta0, mX, vY)  # test function call

# gradient function
def likelihoodScore(vBeta, mX, vY):
    return(np.dot(mX.T, 
                  (logit(mX, vBeta) - vY)))
likelihoodScore(vBeta0, mX, vY).shape # test function call
sp.optimize.check_grad(logLikelihoodLogitVerbose, likelihoodScore, 
                       vBeta0, mX, vY)  # check that the analytical gradient is close to 
                                                # numerical gradient

# optimize the function (without gradient)
optimLogit = scipy.optimize.fmin_bfgs(logLikelihoodLogitVerbose, 
                                  x0 = np.array([-.1, -.03, -.01, .44, .92, .53,
                                            1.8, .71]), 
                                  args = (mX, vY), gtol = 1e-3)

# optimize the function (with gradient)
optimLogit = scipy.optimize.fmin_bfgs(logLikelihoodLogitVerbose, 
                                  x0 = np.array([-.1, -.03, -.01, .44, .92, .53,
                                            1.8, .71]), fprime = likelihoodScore, 
                                  args = (mX, vY), gtol = 1e-3)
#=====================================================