N=int(input())
arr=[]
for i in range(N):
    a=input()
    if a not in arr:
        arr.append(a)
t=0
for i in range(1,20001):
    tmp=[]
    for j in range(len(arr)):  
        if len(arr[j]) == i:
            t+=1
            tmp.append(arr[j])
    if len(tmp) == 1:
        print(*tmp)
    else:
        tmp.sort()
        for k in range(len(tmp)):
            print(tmp[k])
    if t == N:
        break