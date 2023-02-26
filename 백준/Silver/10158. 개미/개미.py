w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = (p + t) // w
b = (q + t) // h
#나눈 몫이 홀수 이면 반대방향 짝수이면 원래방향
# x주기는 w, y주기는 h이므로 
if a % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w
if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)