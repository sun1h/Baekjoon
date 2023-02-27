N=int(input())
arr=list(map(int,input().split()))
tmp=0
total=0
for a in arr:
    tmp=0
    for i in range(1,a):   
        if a % i ==0:
            tmp +=1
    if tmp == 1:
        total+=1
print(total)

