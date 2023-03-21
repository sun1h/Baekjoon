N = int(input())
lst = list(map(int, input().split()))
stack = []
result = [-1 for _ in range(N)]
for i in range(N):
    while stack and stack[-1][1] < lst[i]:
        result[stack[-1][0]] = lst[i]
        stack.pop()
    stack.append([i, lst[i]])
print(*result)
