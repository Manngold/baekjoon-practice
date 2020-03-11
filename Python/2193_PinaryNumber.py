n = int(input())

dp = [1, 1, 2]

if n <= 3:
    pass
else:
    for i in range(3, n):
        dp.append(dp[i - 2] + dp[i - 1])

print(dp[n-1])
