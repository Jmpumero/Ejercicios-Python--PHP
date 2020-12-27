#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    bn=False
    sn=False
    ant=0
    n=0
    v=0
    for i in range(steps):
        
        ant=n
        if path[i]=='U':
            n+=1
        else:
            n-=1
            
        if ant>=0 and  n<0:
            bn=True
        if ant<0 and n>=0:
            sn=True
            
        if bn and sn:
            bn=False
            sn=False
            v+=1
          
    return v
            
     

if __name__ == '__main__':
   

    steps = 8

    path = ['U','D','D','D','U','D','U','U']

    result = countingValleys(steps, path)

  