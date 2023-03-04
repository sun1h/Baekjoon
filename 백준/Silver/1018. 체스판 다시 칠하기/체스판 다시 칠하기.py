N, M = map(int, input().split())
arr = [input() for _ in range(N)]
mn = 64  # 최소값 저장할 변수 (다시 칠해야 하는 최대값 8*8을 처음 지정)
for i in range(N + 1 - 8):  # 8*8 배열만큼 떼어내기
    for j in range(M + 1 - 8):
        tmp_black = 0  # 처음 시작점을 검정색으로 칠할 때 새로 칠해야 하는 경우
        tmp_white = 0  # 처음 시작점을 흰색으로 칠할 때 새로 칠해야 하는 경우
        for k in range(0, 8):
            for s in range(0, 8):
                if (k + s) % 2:  # 처음 시작점에서 거리의 합이 홀수인 경우 -> 시작점과 색깔이 달라야 한다.
                    if arr[i + k][j + s] == 'B':  # 처음 시작점이 검정색이고 거리의 합이 홀수인 지점이 검정색인 경우
                        tmp_black += 1
                    if arr[i + k][j + s] == 'W':
                        tmp_white += 1
                else:
                    if arr[i + k][j + s] != 'B':  # 처음 시작점에서 거리의 합이 짝수인 경우 -> 시작점과 색깔이 같아야 한다.
                        tmp_black += 1
                    if arr[i + k][j + s] != 'W':
                        tmp_white += 1
        if tmp_black < mn:  # 새로 칠해야 하는 수 중 가장 작은 값 출력하기
            mn = tmp_black
        if tmp_white < mn:
            mn = tmp_white
print(mn)
