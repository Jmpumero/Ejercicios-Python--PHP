#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    
    act=((s - 1 + m - 1) % n) + 1
    
        
    return(act)
     

if __name__ == '__main__':
    

   

    n = 7

    m = 19

    s = 2

    result = saveThePrisoner(n, m, s)
    print(result)

        