#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    cad=''
    hora={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',21:'twenty one',22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty eight',29:'twenty nine'}
    
    if m==0:
      cad=hora.get(h)+ " o' clock "
    else:
        if m==30:
          cad="half past "+hora.get(h)
        else:
            if m==15:
                cad="quarter past "+hora.get(h)
            else:
                if m==45:
                  cad="quarter to "+hora.get(h+1)
                else:
                    if m==1:
                       cad="one minute past "+hora.get(h)
                    else:
                        if m>1 and m<30:
                          cad= hora.get(m)+" minutes past "+hora.get(h)
                        else:
                            if m>30:
                                cad= hora.get(60-m)+" minutes to "+hora.get(h+1)
                                
              
    
    return cad

if __name__ == '__main__':
    

    h = 5

    m = 40

    result = timeInWords(h, m)
    print (result)

    
