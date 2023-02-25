#0,0을 기준으로 측정한 거리
def func(a,b):
    if a ==1:
        return b
    elif a==2:
        return x+y+x-b
    elif a==3:
        return 2*x+2*y-b
    else:
        return x+b

x,y=map(int,input().split())
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N+1)]
lst=[]
for i in range(N+1):
    lst.append(func(arr[i][0],arr[i][1]))
total=0
#측정위치에서 시계방향 반시계방향
for i in range(N):
    l1=abs(lst[N]-lst[i])
    l2=2*(x+y)-l1
    total+=min(l1,l2)
print(total)