#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
        nueva=s[0:8]
        h=s[0:2]
        if s.find('AM')==-1:
            if int(h)<12:
                nueva=''
                nueva=str(int(h)+12)+s[2:8]  
        else:
          if int(h)==12:
            nueva=''
            nueva='00'+s[2:8]
     
        return nueva
          
        
       
    

if __name__ == '__main__':
    

    s = "12:05:45PM"

    result = timeConversion(s)
    print(result)

   