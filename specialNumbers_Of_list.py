x = list(map(int,input().strip().split()))

cnt = 0
ans_list = []
for n in x:
    for m in x:
        if (m != n and n%m == 0):
            ans_list.append(n)
            
print (len(list(set(ans_list))))