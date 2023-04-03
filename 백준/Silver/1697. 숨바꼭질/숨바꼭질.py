from collections import deque


def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            return
        for nxt in (x - 1, x + 1, 2 * x):
            if 0 <= nxt < mx and not dist[nxt]:
                dist[nxt] = dist[x] + 1
                q.append(nxt)


mx = 10 ** 5 + 1
N, K = map(int, input().split())
dist = [0 for _ in range(100001)]
bfs()
