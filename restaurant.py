#!/bin/python3

import os
import sys
import math
#
# Complete the restaurant function below.
#
def restaurant(l, b):
    #
    # Write your code here.
    #
    A = l*b
    for x in range(1,A):
        if (x == math.sqrt(A)):
            return (1)
    if (l==b):
        return (1)
    else:
        m = max(l,b)
        n = min(l,b)
        while(n!=0):
            m,n=n,m%n
        gcd = m
        a = l//gcd
        b = b//gcd
        return (a*b)
            
    

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')
        
        print (result)

    fptr.close()
