n, k = map(int, input().split())
girl = [0] * 7
boy = [0] * 7

for i in range(n):
    s,y =map(int, input().split())
    if s == 0:
        girl[y] +=1
    else:
        boy[y] +=1

total=0
for i in range(1,7):
    total+=((girl[i]+(k-1))//k)+((boy[i]+(k-1))//k)

print(total)