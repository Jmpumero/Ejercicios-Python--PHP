#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    h=0
    if n==0:
      return 1
    else:
        h=1
        for i in range(n):
            if i%2!=0:
                h=h+1
            else:
                h=h*2
    return h
           
           

if __name__ == '__main__':
    

    n=4
    result = utopianTree(n)

        
