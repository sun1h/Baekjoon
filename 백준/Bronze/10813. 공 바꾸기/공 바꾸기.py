N,M=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(M)]
lst=[]
for i in range(N+1):
    lst.append(i)
for i in range(M):
    a,b =lst[arr[i][0]],lst[arr[i][1]]
    lst[arr[i][0]]=b
    lst[arr[i][1]]=a
print(*lst[1:])