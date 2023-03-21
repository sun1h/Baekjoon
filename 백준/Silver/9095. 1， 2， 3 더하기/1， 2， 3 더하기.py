def find(n):
    dp = [0] * (n + 1)
    dp[1] = 1  # 1
    if n ==2:
        dp[2] = 2  # 2 / 1+1
    if n==3:
        dp[2] = 2
        dp[3] = 4  # 3/ 1+2 /1+1+1/ 2+1
    if n > 3:
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

T = int(input())
for i in range(T):
    n = int(input())
    print(find(n))
