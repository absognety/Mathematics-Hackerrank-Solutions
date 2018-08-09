#!/bin/python3

import math
import os
import random
import re
import sys

def reversal(n,k):
    lt = list(range(n))
    lt.reverse()
    for i in range(1,n):
        lt_ = lt[i:]
        lt_.reverse()
        lt = lt[0:i] + lt_
    return (lt.index(k))
        


if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    t = int(input())

    for n_iter in range(t):
        
        nk = input().split()
        
        n = int(nk[0])
        
        k = int(nk[1])
        
        result = reversal(n,k)
        
        fptr.write(str(result) + '\n')

    fptr.close()
