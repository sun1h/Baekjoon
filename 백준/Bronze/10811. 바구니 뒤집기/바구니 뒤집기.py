N,M=map(int,input().split())
arr=[i for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    lst_tmp=[]
    for j in range(a,b+1):
        lst_tmp.insert(0,arr[j])
    for j in range(a,b+1):
        arr[j]=lst_tmp[j-a]
print(*arr[1:])