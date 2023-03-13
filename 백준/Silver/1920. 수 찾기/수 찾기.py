N = int(input())
a = set(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
for num in arr:
    print(1) if num in a else print(0)