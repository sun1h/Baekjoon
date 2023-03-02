def check1(x,y,dx,dy):
    global mx
    total=arr[y][x]
    for i in range(4):
        for j in range(1,M):
            nx = x + dx[i] *j
            ny = y + dy[i] *j
            if 0 > nx or 0 > ny or N <= nx or N <= ny:
                continue
            else:
                total+=arr[ny][nx]
    if total > mx:
        mx=total
    return

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    di = [-1, 1, -1, 1]
    dj = [-1, 1, 1, -1]
    mx=0
    for i in range(N):
        for j in range(N):
            check1(i,j,dx,dy)
            check1(i,j,di,dj)
    print(f'#{tc} {mx}')
