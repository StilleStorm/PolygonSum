# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:56:14 2018

@author: StilleStorm
"""

from math import pi as pi, tan as tan


#defining function polucym (n, s)
def polysum(n, s):
    """    
    function sums area and perimeter of a polygon,
    where n is number of sides and s is lenght of a side of given polygon """
   
    #variables for area and square of perimeter
    polyarea = ((0.25*n*(s**2))/(tan(pi/n)))
    polyperimsq = (s*n)**2
    
    #summing up and rounding 
    sum = polyarea + polyperimsq
    sum = round(sum, 4)

    return sum