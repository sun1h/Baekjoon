N=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
total=0
for i in range(len(a)):
    if a[i] >= b:
        a[i] -= b
        total += 1
        if a[i] % c == 0:
            total += (a[i] // c)
        else:
            total += (a[i] // c) + 1
    else:
        total += 1

print(total)
