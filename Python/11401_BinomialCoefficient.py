n, k = map(int, input().split())

dp = []

for i in range (n + 1):
  if i == 0 or i == 1:
    dp.append(1)
  else:
    dp.append(int((dp[i-1] * i) % 1000000007))

answer = int((dp[n] / (dp[k] * dp[n-k])) % 1000000007)

print(answer)