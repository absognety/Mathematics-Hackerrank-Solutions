#!/bin/python3

import os
import sys
import math
#
# Complete the divisors function below.
#
def divisors(n):
    #
    # Write your code here.
    #
    #divisors = [i for i in range(2,n+1,2) if n%i==0]
    #return(len(divisors))
    return(int(not(n%2)) and sum([(n%i==i%2==0) + (n%(n/i)==(n/i)%2==0 and ((n/i)!=i)) for i in range(2,int(math.sqrt(n) + 1))]) + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()

