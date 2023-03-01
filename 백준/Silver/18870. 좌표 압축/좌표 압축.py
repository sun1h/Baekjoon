N=int(input())
arr=list(map(int,input().split()))
a=sorted(list(set(arr)))

dic={x: i for i,x in enumerate(a)}

for ar in arr:
    print(dic[ar], end=' ')
