def gcd(a, b):
    if b == 0:
        return a
    a, b = b, a%b
    return gcd(a, b)

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())
n = n1*d2 + d1*n2
d = d1*d2
g = gcd(max(n,d), min(n,d))
print(n//g, d//g)
