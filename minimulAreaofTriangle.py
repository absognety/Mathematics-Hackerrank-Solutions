import sys
import math
def lowestTriangle(base, area):
    # Complete this function
    h = (math.ceil(2*area/base))
    return h
base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
