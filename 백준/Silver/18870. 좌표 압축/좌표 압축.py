N=int(input())
arr=list(map(int,input().split()))

a=sorted(list(set(arr)))
# for ar in arr:
#     print(a.index(ar),end=' ')

numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i

for i in arr:
    print(numdict[i], end=' ')