"""Functions used in the Introduction to Quantitative Geology course"""

import math
import numpy as np

# Define your new functions below
def gaussian(xbar, sigma, x):
    '''
    Computes the Gaussian function.
    ---------------------------
    Arguments:
        xbar <float> -- mean of the Gaussian distribution
        sigma <float> -- standard deviation of Gaussian distribution
        x <float> -- set of x-axis values  
    ----------------------------
    Returns:
        <float> Set of y-axis values for the Gaussian function
    '''
    array = np.zeros(len(x))

    for i in range(len(x)) :
        e = -((x[i] - xbar)**2) / (2 * sigma**2)
        array[i] = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(e)           
        return array


def linregress(x, y):
    '''
    Computes the unweighted linear regression (best-fit) line 
    using delta, A and B from given x and y values.
    ---------------------------
    Arguments:
        x <float> -- set of x-axis values
        y <float> -- set of y-axis values
    ----------------------------
    Returns:
        A <float> -- y-intercept of best-fit line
        B <float> -- slope of best-fit line
    '''  
    delta = np.sum(len(x) * (x**2)) - (np.sum(x)**2)
    A = ((np.sum(x**2) * np.sum(y) - (np.sum(x) * np.sum(x*y)))) / delta
    B = ((len(x)*np.sum(x*y)) - (np.sum(x)) * np.sum(y)) / delta
    return A, B


def pearson(x, y):
    '''
    Computes the Pearson correlation coefficient (r) to determine 
    the linear relationship between two variables x and y.
    ---------------------------
    Arguments:
        x <float> -- set of x-axis values
        y <float> -- set of y-axis values
    ----------------------------
    Returns:
        r <float> -- Pearson correlation coefficient
    '''
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    num = np.sum((x - mean_x)*(y - mean_y)) 
    denom_1 = np.sum((x - mean_x)**2)
    denom_2 = np.sum((y - mean_y)**2)  
    r = num/np.sqrt(denom_1*denom_2)
    return r


def chi_squared(obs, exp, std):
    '''
    Computes chi-squared value to assess goodness-of-fit 
    between observed and expected values.
    ---------------------------
    Arguments:
        obs <float> -- observed values
        exp <float> -- expected values from linear regression line 
        std <float> -- standard deviation of observed values
    ----------------------------
    Returns:
        chi_squared <float> -- weighted sum of the squared errors
    '''
    numerator = sum((obs[i] - exp[i])**2 / std[i]**2 for i in range(len(obs)))
    chi_squared = numerator/(len(obs))
    return chi_squared