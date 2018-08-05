#!/bin/python3
import os

# Complete the solve function below.
def solve(n, m):
    mi = min(n,m)
    ma = max(n,m)
    return ((mi*ma)-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()