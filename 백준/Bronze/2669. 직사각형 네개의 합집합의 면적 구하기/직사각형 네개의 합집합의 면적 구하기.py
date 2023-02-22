arr=[[0 for _ in range(101)] for _ in range(101)]

for i in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            if arr[x][y] != 1:
                arr[x][y] = 1
total=0
for i in range(101):
    total+=arr[i].count(1)
print(total)