#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#



def climbingLeaderboard(ranked, player):
    # Write your code here
    band=True
    poss=1
    j=0
    i=0
    re=[]
    
     
    for item in reversed(player):
        band=True
        
        while band:
            if item>= ranked[j]:
                
                re.insert(0,poss)
                band=False
                
            else:
                
                if j==0:
                    poss+=1
                    
                else:
                    
                    if ranked[j-1]!= ranked[j]:
                        poss+=1
                    
                    
                j+=1 
                
            if j>= len(ranked):
                band=False 
                re.insert(0,poss)
            
                
        i+=1
        
             
                
    return re
         
     

if __name__ == '__main__':
   
    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5,25, 50, 120]
    #player = [50]
    result = climbingLeaderboard(ranked, player)

    print(result)