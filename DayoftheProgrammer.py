#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def leapyn(year):
    band=False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        band=True
    
    return band

def leapyj(year):
    band=False
    if year % 4 == 0 :
        band=True
    
    return band
    
def dayOfProgrammer(year):
    cad=''
    if year==1918:
      cad='26.09.1918'
    else:
        if year>=1700 and year<=1917 :
            if leapyj(year):
                cad='12.09.'+str(year)
            else:
                cad='13.09.'+str(year)
        else:
            if leapyn(year):
                cad='12.09.'+str(year)
            else:
                cad='13.09.'+str(year)
                
    return cad
            

        
        
        

if __name__ == '__main__':
   

    year = 1918

    result = dayOfProgrammer(year)
    print (result)

   
