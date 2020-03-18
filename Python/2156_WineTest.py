n = int(input())

wine = []

for _ in range(n):
    wine.append(int(input()))

dp = [0]
dp.append(wine[0])

if n > 1:
    dp.append(wine[0] + wine[1])

for i in range(3, n + 1):
    one = wine[i - 1] + dp[i - 2]
    two = wine[i - 1] + wine[i - 2] + dp[i - 3]
    three = dp[i - 1]
    dp.append(max(one, two, three))

print(dp[-1])
