N=int(input())
arr=[[0 for _ in range(101)] for _ in range(101)]

for i in range(1,N+1):
    x1,y1,w,h = map(int,input().split())
    for x in range(x1,x1+w):
        for y in range(y1,y1+h):
            if arr[x][y] < i:
                arr[x][y] = i


for i in range(1,N+1):
    tmp=0
    for j in range(101):
        tmp+=arr[j].count(i)
    print(tmp)
