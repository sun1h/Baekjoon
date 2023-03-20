N, M = map(int, input().split())
h = list(map(int, input().split()))
start, end = 1, max(h)  # 1을 시작, 최댓값을 끝

while start <= end: # 반복문 종료 조건
    mid = (start + end) // 2
    total = 0  # 잘린 나무 높이 총합
    for H in h:
        if H > mid:
            total += H - mid
    #이진탐색
    if total >= M:
        start = mid+1 # 잘린 나무 높이 총함이 M이상 이면 중앙값+1 ~ 끝 값 다시 찾기
    else:
        end = mid-1 # 잘린 나무 높이 총함이 M미만 이면 시작-1 ~ 중앙값 값 다시 찾기
print(end)