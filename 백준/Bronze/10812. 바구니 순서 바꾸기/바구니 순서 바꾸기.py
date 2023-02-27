N,M=map(int,input().split())
arr=[i for i in range(N+1)]
for _ in range(M):
    i,j,k=map(int,input().split())
    tmp=arr[k:j+1]+arr[i:k]
    for n in range(i,j+1):
        arr[n] = tmp [n-i]
print(*arr[1:])
    
       
