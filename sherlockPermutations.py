#!/bin/python3

import os
import sys
import math
def factorial(n):
    if(n==0):
        return (1)
    else:
        return (n*factorial(n-1))

# Complete the solve function below.
def solve(n, m):
    #x = m+n-1
    #y = factorial(x)
    #z = factorial(m-1)
    #w = factorial(n)
    #return ((y//(z*w))%(10**9 + 7))
    return ((math.factorial(m+n-1)//(math.factorial(n)*math.factorial(m-1)))%1000000007)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()