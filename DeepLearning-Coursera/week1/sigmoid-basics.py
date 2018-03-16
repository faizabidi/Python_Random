import math
import numpy as np 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""calculate sigmoid function using math library and without it. In DL, we mostly never use the math library to calculate the sigmoid function."""

def basicsigmoid(x):
    s = 1 / (1 + math.exp(-x))
    return s

print basicsigmoid(3)

def basicsigmoid_np(x):
    s = 1 / (1 + np.exp(-x))
    return s

print basicsigmoid_np(3)

# numpy also lets do do things like below
x = np.array([1, 2, 3])
print basicsigmoid_np(x)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""sigmoid_derivative(x)=sigma_fx(x)*(1-sigma_fx(x))"""
def sigmoid_derivative(x):
    s = 1 / (1 + np.exp(-x))
    ds = s * (1 - s)
    return ds

x = np.array([1, 2, 3])
print ("sigmoid_derivative(x) = " + str(sigmoid_derivative(x)))