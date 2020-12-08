#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
   
    total=0
    dp=0
    ds=0
    n=len(arr)
    dp=sum(arr[i][i] for i in range(n))
    ds=sum(arr[i][(n-1)-i] for i in range(n))
    total=abs(dp-ds)
    return total

if __name__ == '__main__':
    #fptr = open('diagonald.txt', 'w')

    #n = int(input().strip())

    arr = [[11,2,4],[4,5,6],[10,8,-12]]

    '''for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))'''

    result = diagonalDifference(arr)
    print (result)
    
    #fptr.write(str(result) + '\n')

    