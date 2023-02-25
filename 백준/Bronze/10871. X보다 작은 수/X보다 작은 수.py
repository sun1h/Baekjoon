N,X=map(int,input().split())
arr=list(map(int,input().split()))
lst=[]
for i in range(N):
    if arr[i] < X:
        lst.append(arr[i])
print(*lst)