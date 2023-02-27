N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
dp=[0 for _ in range(1001)]
mx,x=0,0
for a in arr:
    dp[a[0]] = a[1]
    if mx < a[1]:
        mx=a[1]
        x=a[0]
t=0
total=0
pre=0
for i in range(x):
    if dp[i] != 0:
        if dp[i] > pre:
            t = dp[i]
            pre=dp[i]
    total+=t
t=0
pre=0
for i in range(x,len(dp))[::-1]:
    if dp[i] != 0:
        if dp[i] > pre:
            t = dp[i]
            pre=dp[i]
    total+=t

print(total)