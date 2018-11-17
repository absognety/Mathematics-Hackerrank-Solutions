#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr,n):
    sum_diag1 = 0
    sum_diag2 = 0
    for i in range(len(arr)):
        sum_diag1=sum_diag1+arr[i][i]
    for i in range(len(arr)):
        sum_diag2 = sum_diag2+arr[i][n-i-1]
    diff = abs(sum_diag1-sum_diag2)
    return (diff)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()

