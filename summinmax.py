import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    
    print(str(sum(arr)-max(arr))+" "+ str(sum(arr)-min(arr)))

if __name__ == '__main__':
    arr =  arr = [11,2,4,4,5,6,10,8,-12]

    miniMaxSum(arr)