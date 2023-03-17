def func(K):
    global total
    tmp = []
    for i in range(N)[::-1]:
        if len(str(K)) >= len(str(arr[i])):
            tmp.append(arr[i])
    idx = 0
    while K > 0:
        if K == 0:
            return
        elif K >= tmp[idx]:
            K -= tmp[idx]
            total += 1
        else:
            idx += 1

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)] #동전의 가치 (오름차순)
total = 0 # 필요한 동전 갯수
func(K) #함수호출
print(total)
