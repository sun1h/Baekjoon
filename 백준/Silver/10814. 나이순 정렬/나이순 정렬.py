N=int(input())
arr=[]

for i in range (N): 
    a,b = input().split() 
    arr.append([int(a), b])

arr.sort(key=lambda x:x[0])

for i in range(N):
    print(*arr[i])