N=int(input())
arr=[list(map(int,input().split())) for _ in range(6)]
x=[]
y=[]
for i in range(6):
    if arr[i][0]==3 or arr[i][0]==4:
        x.append(arr[i][1])
    else:
        y.append(arr[i][1])
lst=[]
for i in range(6):
    if arr[i][0] == arr[(i+2)%6][0]:
        lst.append(arr[(i+1)%6][1])
    
print((max(x)*max(y)-lst[0]*lst[1])*N)
