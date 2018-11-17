#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = [i for i in arr if i > 0]
    neg = [i for i in arr if i < 0]
    zer = [i for i in arr if i == 0]
    num_pos = len(pos)/len(arr)
    num_neg = len(neg)/len(arr)
    num_zer = len(zer)/len(arr)
    for i in [num_pos,num_neg,num_zer]:
        print ("{0:.6f}".format(i))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
