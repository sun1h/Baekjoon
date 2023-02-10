N=list(map(int,input().split()))
t=0
for i in range(len(N)):
    if N.count(N[i])==3:
        t=10000+N[i]*1000
        break
    elif N.count(N[i])==2:
        t=1000+N[i]*100
        break
    else:
        t=max(N)*100
print(t)