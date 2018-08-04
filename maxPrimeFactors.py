#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    #
    # Write your code here.
    #
    h=0
    c=1
    i=2
    while(c*i<=n):
        t=False
        for x in range(2,int(i**0.5)+2):
            if i%x==0:
                t=False
                break;
            else:
                t=True
                    
        if t or i==2:
            c=c*i
            h+=1
        i=i+1
    return h
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
