#!/bin/python3

import os
import sys
import math
#
# Complete the movingTiles function below.
#
def movingTiles(l, s1, s2, queries):
    #
    # Write your code here.
    res = []
    for q in queries:
        num = math.sqrt(2)*abs(math.sqrt(q)-l)
        den = abs(s1-s2)
        res.append(num/den)
    return(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()