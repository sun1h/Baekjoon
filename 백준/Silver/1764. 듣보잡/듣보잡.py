N,M=map(int,input().split())
l=[input() for _ in range(N)]
s=[input() for _ in range(M)]
lst = list(set(l) & set(s))
print(len(lst))
lst.sort()
for ls in lst:
    print(ls)