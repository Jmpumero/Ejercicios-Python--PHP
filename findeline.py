#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    p=0
    neg=0
    c=0
    for item in arr:
        #print(item)
        if item>0:
          p+=1
        else:
            if item<0:
              neg+=1
            else:
                c+=1
        
    print( format(p/n, '.10f'))
    print( format(neg/n, '.10f'))
    print( format(c/n, '.10f'))
     
    

if __name__ == '__main__':
    

    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
