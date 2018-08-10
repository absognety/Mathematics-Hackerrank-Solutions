#!/bin/python3

import os
import sys

#
# Complete the strangeGrid function below.
#
def strangeGrid(r, c):
    #
    # Write your code here.
    #
    if (r%2 != 0):
        first_term=10*(r-1-(r//2))
        return(first_term + (c-1)*2)
    else:
        first_term = 1+((r//2)-1)*10
        return (first_term + (c-1)*2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()