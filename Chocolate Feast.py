#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    t=0
    choco=n//c
    wp=choco
    extra=wp//m
    while wp>=m:
        extra = extra+(wp//m + wp%m)//m
        wp = wp//m
        #r=sobra//m
        #t+=r
        #sobra=sobra-m+r
    return choco+extra

if __name__ == '__main__':
    


    n = 43203

    c = 60

    m = 5

    result = chocolateFeast(n, c, m)
    print(result)

        