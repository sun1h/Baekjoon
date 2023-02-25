def func(arr,b):
    for i in range(6):
        if b==arr[i]:
            idx=i
            break
    
    if idx == 0:
        return (max(arr[1],arr[2],arr[3],arr[4]) , arr[5])
    elif idx == 5:
        return (max(arr[1],arr[2],arr[3],arr[4]) , arr[0])
    elif idx == 1:
        return (max(arr[0],arr[2],arr[5],arr[4]) , arr[3])
    elif idx == 3:
        return (max(arr[0],arr[2],arr[5],arr[4]) , arr[1])
    elif idx == 2:
        return (max(arr[0],arr[1],arr[5],arr[3]), arr[4])
    elif idx == 4:
        return (max(arr[0],arr[1],arr[5],arr[3]), arr[2])


N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
mx=0
for i in range(1,7):
    total=0
    for j in range(N):
        tmp,idx=func(arr[j],i)
        i=idx
        total+=tmp
    if mx < total:
        mx=total
print(mx)