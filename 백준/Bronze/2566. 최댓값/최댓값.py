arr=[list(map(int,input().split())) for _ in range(9)]
mx=0
x=0
y=0
for i in range(9):
    for j in range(9):
        if mx < arr[i][j]:
            mx=arr[i][j]
            x=j
            y=i
print(mx)
print(y+1,x+1)