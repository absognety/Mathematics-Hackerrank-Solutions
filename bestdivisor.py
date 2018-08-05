#!/bin/python3

import math
import os
import random
import re
import sys

def sum_of_digits(num):
    total=0
    while(num>0):
        dig=num%10
        total+=dig
        num=num//10
    return (total)

def bestDivisor(n):
    divisors = []
    for i in range(1,n+1):
        if (n%i == 0):
            divisors.append(i)
    sum_digits = []
    for m in divisors:
        sum_digits.append(sum_of_digits(m))
    maximum = max(sum_digits)
    if (sum_digits.count(maximum)==1):
        ind = sum_digits.index(maximum)
        return (divisors[ind])
    else:
        divs = [divisors[i] for i in range(len(sum_digits)) if sum_digits[i] == maximum]
        mi = min(divs)
        return (mi)

    
if __name__ == '__main__':
    n = int(input())
    result = bestDivisor(n)
    print (result)
