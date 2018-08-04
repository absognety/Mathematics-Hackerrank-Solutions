import os
import sys

#Reflection of a point wrt to another point
# Complete the findPoint function below.
#
def findPoint(px, py, qx, qy):
    rx = 2*qx - px
    ry = 2*qy - py
    r = [rx, ry]
    return (r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        pxPyQxQy = input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
