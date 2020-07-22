n = int(input())

ports = list(map(int, input().split()))

for i in range(n):
    ports[i] = (ports[i], i+1)

ports.sort()

dp = [0]*n

for i in range(n):
    idx = ports[i][1]
    mv = 0
    for j in range(idx):
        if dp[j] > mv:
            mv = dp[j]
    dp[idx-1] = mv+1

print(max(dp))
