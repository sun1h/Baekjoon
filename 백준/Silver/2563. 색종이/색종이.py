N=int(input())
visit=[[False for _ in range(101)] for _ in range(101)]

for _ in range(N):
    h,v=map(int,input().split())
    for i in range(10):
        for j in range(10):
            visit[h+i][v+j] = True

total=0
for i in range(101):
    total+=visit[i].count(True)

print(total)