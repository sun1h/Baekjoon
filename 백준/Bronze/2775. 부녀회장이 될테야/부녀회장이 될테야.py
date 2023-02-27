T=int(input())
for _ in range(T):
    k=int(input())
    n=int(input())
    ground=[i for i in range(1,n+1)]
    for _ in range(k):
        for i in range(1,n):
            ground[i] +=ground[i-1]
    print(ground[-1])