import math
import os
import random
import re
import sys

# Complete the staircase function below.
def imprime(n):
    for i in range(n):
        t+='#'
def staircase(n):
    if n==1:
      print('#')
    else:
      staircase(n-1)
      imprime(n)
      
if __name__ == '__main__':
    n = 2

    staircase(n)