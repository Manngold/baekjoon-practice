n = int(input())

for _ in range(n):
    dest = int(input())
    dp = [0, 1, 1, 1]
    for i in range(4, dest + 1):
        dp.append(dp[i-3] + dp[i-2])

    print(dp[dest])
