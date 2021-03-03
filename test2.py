#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def desencolar(cad):
   new=''
   new=cad[1:len(cad)]
   return new

def remult(cad,old,n,j):
    ult=0
    new=''
    ult=cad.rfind(str(old))
    if ult!=-1:
        #print('uy:'+str(old)+str(n))
        new=desencolar(cad[0:ult]+str(n)+cad[ult+1:len(cad)])
        j-=1
    else:
        new=cad
    
    return new,j

def islowercase(a):
    b=False
    if (ord(a)>=97 and ord(a)<=122):
           b=True  
    return b

def isupercase(a):
    b=False
    if (ord(a)>=65 and ord(a)<=90):
           b=True  
    return b

def swap(s,a,b,i,j):
    
    new=s[0:i]+b+a+s[j+1:len(s)]
    #print(new)
    return new

def decryptPassword(s):
    # Write your code here 
    i=0
   
    while i<len(s):
        
        try:
            t=int(s[i])
            #print('valor:'+str(t))
            if t!=0:
                s,i=remult(s,'0',t,i)
            
        except ValueError as identifier:
             
             if (isupercase(s[i])and islowercase(s[i+1])):
                s=swap(s,s[i],s[i+1],i,i+1)
                
                 
              
            
        #print(new +' '+str(i))
        i+=1
        
        
    
    print(s.replace('*', ''))
    #print(j)
if __name__ == '__main__':
    

    s ='51Pa*0Lp*0e'
    t='pTo*Ta*0'

    result = decryptPassword(t)

    