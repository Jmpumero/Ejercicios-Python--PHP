import math
import os
import random
import re
import sys

# Complete the staircase function below.

def staircase(n):
    t=''
    for index in range(n):
      t+='#'
      print(t)
      
     
def staircase_rigth(n):
    t=''
    for i in range(n):
     
      for index in range(n-(i+1)):
        t+=' '
      
      for item in range(i+1):
        t+='#' 
      print(t)
      t=''  
      
      
if __name__ == '__main__':
    n = 6

    staircase_rigth(n)