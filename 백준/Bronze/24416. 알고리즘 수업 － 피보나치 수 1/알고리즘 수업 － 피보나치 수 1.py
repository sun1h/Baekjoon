def fib(n):
    global a
    a+=1
    if n==1 or n==2:
        a-=1
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibo(n):
    global f,b
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2]
        b+=1
    return f[n-1]

n=int(input())
f=[1 for _ in range(41)]
a,b=1,0
fib(n)
fibo(n)
print(a,b)