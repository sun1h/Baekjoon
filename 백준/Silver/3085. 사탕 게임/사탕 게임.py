def find(arr):
    mx=1
    for i in range(N):
        tmp=1
        for j in range(1,N):
            if arr[i][j] == arr[i][j-1]:
                tmp+=1
            else:
                tmp=1
            if tmp > mx:
                mx = tmp
        tmp=1
        for j in range(1,N):
            if arr[j][i] == arr[j-1][i]:
                tmp+=1
            else:
                tmp=1
            if tmp > mx:
                mx = tmp
    return mx

N=int(input())
arr=[[] for _ in range(N)]
for i in range(N):
    a = input()
    for j in range(N):
        arr[i].append(a[j])
mx=0
for i in range(N):
    for j in range(N):
        if j+1<N:
            # 가로줄 전부 바꾸기
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
            tmp=find(arr)
            if tmp > mx:
                mx= tmp
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
        if i + 1 < N:
            # 세로줄 전부 바꾸기
            arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j]
            tmp2=find(arr)
            if tmp2 >mx:
                mx=tmp2
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
print(mx)
