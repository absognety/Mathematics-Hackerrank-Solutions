#!/bin/python3

import os
import sys
import math
#
# Complete the gameWithCells function below.
#
def gameWithCells(n, m):
    #
    # Write your code here.
    #
    #dim = n*m
    #quot_dim = dim//4
    #rem_dim = dim%4
    #if (rem_dim == 0):
    #    if (n%2 == m%2 == 0):
    #        return (quot_dim)
    #    else:
    #        for s in [n,m]:
    #            if (s >= 4):
    #                if (s%2 == 0):
    #                    return (quot_dim + (s//4))
    #else:
    #    return (quot_dim + rem_dim)
    return ((n+(n%2))*(m+(m%2))//4)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
