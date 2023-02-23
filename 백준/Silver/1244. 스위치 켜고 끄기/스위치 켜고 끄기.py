N=int(input())
arr=list(map(int,input().split()))
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a == 1:
        k=b
        while k <= N:
            if arr[k-1] == 0:
                arr[k-1] = 1    
            else:
                arr[k-1] = 0
            k= k+b
    else:
        lst=[False for _ in range(N)]
        for i in range(min(N+1-b,b)):
            if arr[b-1-i] == arr[b-1+i]:
                lst[b-1-i] = True
                lst[b-1+i] = True
            else:
                break
        for i in range(len(lst)):
            if lst[i] == True:
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i]=0
 
if N <=20:
    print(*arr[:20])
elif N <=40:
    print(*arr[:20])
    print(*arr[20:40])
elif N<=60:
    print(*arr[:20])
    print(*arr[20:40])
    print(*arr[40:60])
elif N<=80:
    print(*arr[:20])
    print(*arr[20:40])
    print(*arr[40:60])
    print(*arr[60:80])
else:
    print(*arr[:20])
    print(*arr[20:40])
    print(*arr[40:60])
    print(*arr[60:80])
    print(*arr[80:100])

