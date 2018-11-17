
arr = [3,19,12,89,-1,10,11,-19,0,1,20,35,49,21,80,93]
arr = sorted(arr)
low = 0
high = len(arr)
import math

def binarySearch(low,high,value):
    
    while (low<=high):
        mid = math.floor((high+low)/2)
        if (arr[mid]<value):
            low=mid+1
        elif (arr[mid]>value):
            high=mid-1
        else:
            return mid
        
    return -1

