#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def num( valor):
    m=0
    m=valor//5
    if(m==0):
        m=1*5
    else:
        m=(m+1)*5
    return m
def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        g=num(grades[i])
        if (g- grades[i] )<3:
            if g>=40:
                grades[i]=g
    return grades
            
                
        
     

if __name__ == '__main__':
   
    

    grades = [73,67,38,33]

 

    result = gradingStudents(grades)
    print(result)

    