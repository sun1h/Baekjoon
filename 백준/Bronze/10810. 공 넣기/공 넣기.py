N,M=map(int,input().split())
arr=[list(map(int, input().split())) for _ in range(M)]
lst=[0]*(N+1)
for i in range(M):
    for j in range(arr[i][0],arr[i][1]+1):
        lst[j]=arr[i][2]
print(*lst[1:])