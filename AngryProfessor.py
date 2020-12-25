#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    cont=0
    r=''
    i=0
    
    for item in a:
        if item<=0:
          cont+=1
          
          
    
    if cont>=k:
      r='NO'
    else:
        print (cont)
        r='YES'
        
    return r
     

if __name__ == '__main__':
    

    
    k = 3

    a = [-1,-3,4,2]

    result = angryProfessor(k, a)
    print(result)

       
