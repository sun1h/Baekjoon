N, M = map(int, input().split())
h = list(map(int, input().split()))
start, end = 1, max(h)  # 1을 시작, 최댓값을 끝
result = 0  # 출력해야 하는 절단기 높이
while start <= end:  # 반복문 종료 조건
    mid = (start + end) // 2  # 중앙 원소 고르기
    total = 0  # 잘린 나무 높이 총합
    for H in h:
        if H > mid:  # 나무 높이가 절단기 높이 보다 커야 잘림
            total += H - mid
    if total >= M:
        result = mid
        start = mid + 1  # 잘린 나무 높이 총함이 M이상 이면 중앙값+1 ~ 끝 값 다시 찾기
    else:
        end = mid - 1  # 잘린 나무 높이 총함이 M미만 이면 시작-1 ~ 중앙값 값 다시 찾기
print(result)
