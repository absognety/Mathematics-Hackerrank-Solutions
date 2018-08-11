#!/bin/python3

import os
import sys
import math


def find (x,y):
    if (x>y):
        return (1)
    else:
        return (math.pow(arr[x-1],find(x+1,y)))
    
# Complete the solve function below.
def solve(arr, queries):
    ans_list = []
    for lt in queries:
        ans = find(lt[0],lt[1])
        if (ans%2==0):
            ans_list.append('Even')
        else:
            ans_list.append('Odd')
    return (ans_list)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
    
#%%
#!/bin/python3

import os
import sys
import math


def find (x,y,arr):
    if (x>y):
        return (1)
    else:
        return (math.pow(arr[x-1],find(x+1,y,arr)))
# Complete the solve function below.
def solve(arr, queries):
    ans_list = []
    for lt in queries:
        if (arr[lt[0]-1]%2!=0):
            ans_list.append('Odd')
        else:
            if lt[0]==arr_count:
                ans_list.append('Even')
            else:
                if (arr[lt[0]]==0 and (lt[1]-lt[0])>0):
                    ans_list.append('Odd')
                else:
                    ans_list.append('Even')
    #ans = find(lt[0],lt[1])
    #    if (ans%2==0):
    #        ans_list.append('Even')
    #    else:
    #        ans_list.append('Odd')
    return (ans_list)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    
    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()


