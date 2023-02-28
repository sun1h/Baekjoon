def check(a,b):
    if arr[a] != arr[b]:
        return a+1,b-1   
    if a == 0 or b == N-1:
        return a,b
    if arr[a] == arr[b]:
       return check(a-1,b+1)

N=int(input())
arr=list(map(int,input().split()))
n=int(input())
for _ in range(n):
    sex, switch = map(int,input().split())
    if sex == 1:
        for i in range(switch-1,N,switch):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
    if sex == 2:
        a,b=check(switch-1,switch-1)
        for i in range(a,b+1):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0

for i in range(0,N,20):
    print(*arr[i:i+20])