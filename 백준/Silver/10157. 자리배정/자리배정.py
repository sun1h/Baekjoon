def move(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visit = [[False]*C for _ in range(R)]
    k = 0
    for i in range(1,C*R+1) :
        if i == K:
           return (x+1,y+1)
        else:
            visit[y][x] = True
            x += dx[k]
            y += dy[k]
            if x<0 or y<0 or x>=C or y>=R or visit[y][x]:
                x -= dx[k]
                y -= dy[k]
                #범위 벗어나면 뒤로 뺐다가 방향 바꿔서 전진 
                k = (k+1)%4
                x += dx[k]
                y += dy[k]


C,R = map(int,input().split())
K = int(input())

#좌석을 줄 수 없는 경우 
if K > C*R :
    print(0)
    exit() #아예끝내기

print(*move(0,0))
