n = int(input())

dp = [1, 3]

for i in range(2, 100001):
  dp.append((dp[i-1] * 2 + dp[i - 2])% 9901)

print(dp[n])
