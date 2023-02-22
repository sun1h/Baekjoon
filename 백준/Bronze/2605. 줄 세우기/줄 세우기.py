N=int(input())
arr=list(map(int,input().split()))
lst=[]
for i in range(0,N):
    if arr[i] == 0:
        lst.append(i+1)
    else:
        for j in range(1,N):
            if arr[i] == j:
                lst.insert(i-j,i+1)
                break
print(*lst)