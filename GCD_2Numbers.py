a = int(input())
b = int(input())

#GCD of two numbers#

def f(a,b):
    if (a==b):
        return (a)
    else:
        maxi = max(a,b)
        mini = min(a,b)
        while(mini):
             maxi,mini = mini,maxi%mini
             ans = maxi
        return (ans)