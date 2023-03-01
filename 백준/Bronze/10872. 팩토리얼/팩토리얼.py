def f(n):
    global ans
    if n == 0:
        return 1
    if n == 1:
        return ans
    ans=ans*n
    return f(n-1)    
N=int(input())
ans=1
print(f(N))