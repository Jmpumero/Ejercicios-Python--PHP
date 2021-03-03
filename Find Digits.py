#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.

def findDigits(n):
    
    #l=list(map(int, str(n)))
    #l=list(filter(lambda numero : numero!=0,l))
    
    return len([i for i in list (map(int, str(n))) if i != 0 and n % i == 0])
    

if __name__ == '__main__':
   

    result = findDigits(106108048)
    print(result)

      