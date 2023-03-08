N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
for i in range(len(arr)):
    cnt = 1  # 1등 부터 시작하므로
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:  # 키와 몸무게 둘다 작다면
            cnt += 1
    lst.append(cnt)
print(*lst)
