#!/bin/python3

import os
import sys
import itertools
# Complete the solve function below.
#itertools and functools - permutations and combinations modules
def solve(n):
    for k in itertools.count(1):
        v = int(bin(k)[2:].replace('1', '9'))
        if not v%n: break
    return(str(v))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
