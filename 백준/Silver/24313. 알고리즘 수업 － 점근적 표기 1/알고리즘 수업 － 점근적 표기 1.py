a, b = map(int, input().split())
c = int(input())
n = int(input())

if c < a :
    print(0)
else :
    if a*n+b <= c*n : print(1)
    else : print(0)