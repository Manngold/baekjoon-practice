n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
  w, v = map(int, input().split())
  for j in range(1, k+ 1):
    if i == 0:
      if j >= w:
        dp[i][j] = v
    else:
      dp[i][j] = dp[i - 1][j]
      if j >= w:
        dp[i][j] = max(dp[i][j],dp[i-1][j-w] + v)
        
print(dp[n][k])
