"""Functions used in the Introduction to Quantitative Geology course"""

# Import any modules needed in your functions here
import math
import numpy as np

# Define your new functions below

'''
    Compute the Gaussian function.
    
    ---------------------------
    
    Arguments:
        xbar -- mean of the Gaussian distribution
        sigma -- standard deviation of Gaussian distribution
        x -- set of x-axis values
        
    ----------------------------
    
    Returns:
        Set of y-axis values for the Gaussian function
'''

def gaussian(xbar, sigma, x):

    array = np.zeros(len(x))

    for i in range(len(x)) :
        e = -((x[i] - xbar)**2) / (2 * sigma**2)
        array[i] = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(e)
               
    return array

