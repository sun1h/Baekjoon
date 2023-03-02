N,M=map(int,input().split())
arr=list(map(int,input().split()))
lst=[]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and  k != i:
                if arr[i] + arr[j] + arr[k] <= M:
                    lst.append(M-(arr[i] + arr[j] + arr[k]))
                    lst.append((arr[i] + arr[j] + arr[k]))
mn=M
x=0
for i in range(0,len(lst),2):
    if mn >= lst[i]:
        mn=lst[i]
        x=i
print(lst[x+1])