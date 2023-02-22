N=int(input())
arr=[[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1,N+1):
    x1,y1,w,h = map(int,input().split())
    for x in range(x1,x1+w):
        for y in range(y1,y1+h):
            arr[x][y] = i
lst=[0]*101
for i in range(1001):
    for j in range(1001):
        lst[arr[i][j]] +=1 

for i in range(1,N+1):
    print(lst[i])