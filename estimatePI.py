#!/usr/bin/python3
#File name: estimatePI.py Assignment 1
#Author: Tom Are Tørum
#Submission: Assignement 1
from math import sqrt
from time import time
def archimedespi(iterations):
    """
        Estimates pi using Archmedes method
    
    Args:
        param1 (int) Number of iterations.

    Returns:
        (float,int) pi, number of sides.
    """
    #Start vaules for number of sides (n) and length of the side (s)
    n = 6
    s = 1.0
    #Loops through the defined iterations
    for i in range(0, iterations):
        pi = (n*s)/2
        a = sqrt(1-(s/2)**2)
        b = 1-a
        s = sqrt(b**2+(s/2)**2)
        n = n*2
    return pi, int(n/2)
start_time = time()
#Calling function archimedespi with 20 iterations
pinumberofsides = archimedespi(20)
end_time = time()
print('Estimated pi: ' + str(pinumberofsides[0]) + ' for ' + str(pinumberofsides[1]) + ' number of sides.')
print('Function execution time ' + str(end_time-start_time))
