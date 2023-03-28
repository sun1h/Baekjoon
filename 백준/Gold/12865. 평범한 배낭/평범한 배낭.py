N,K=map(int,input().split())
lst=[[0, 0]]
for _ in range(N):
    lst.append(list(map(int, input().split())))
dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        weight = lst[i][0]
        value = lst[i][1]
        # 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
        if j < weight:
            dp[i][j]=dp[i-1][j]
        else: # 그렇지 않다면, 다음 중 더 나은 가치를 선택하여 넣는다
            # 현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다. vs 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[N][K])