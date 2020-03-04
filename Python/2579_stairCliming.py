n = int(input())

score = []

for _ in range(n):
    score.append(int(input()))

dp = []

dp.append(score[0])
dp.append(dp[0] + score[1])
dp.append(max(dp[0]+score[2], score[1] + score[2]))

for i in range(3, n):
    dp.append(max(score[i] + score[i - 1] + dp[i - 3], score[i] + dp[i - 2]))

print(dp[-1])
