def prime(k):
    if k==1:
        return False
    for i in range(2,int(k**0.5)+1):
        if k % i ==0:
            return False
    return True

for i in range(int(input())):
    n=int(input())
    for j in range(n//2,0,-1):
        if prime(j) and prime(n-j):
            print(j,n-j)
            break