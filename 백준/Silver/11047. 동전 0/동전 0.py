N, K = map(int, input().split())
lst = []
total = 0

for i in range(N):
    lst.append(int(input()))  # [50000,10000,5000,1000,500,100,50,10,5,1]

for i in range(N)[::-1]:
    if K - lst[i] >= 0:
        total += K // lst[i]  # 몫 만큼 빼준다.
        K = K % lst[i]  # 나머지가 K가 된다.
    if K == 0: # 0이되면 멈춘다.
        break

print(total)