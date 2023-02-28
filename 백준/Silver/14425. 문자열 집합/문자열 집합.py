N,M=map(int,input().split())
S=[input() for _ in range(N)]
search=[input() for _ in range(M)]
total=0
for s in search:
    if s in S:
        total+=1
print(total)