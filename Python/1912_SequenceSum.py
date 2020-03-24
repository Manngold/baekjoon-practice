n = int(input())
arr = list(map(int, input().split()))

dp = []
dp.append(arr[0])
tempMax = arr[0]

for i in range(1, n):
    if arr[i] < dp[i - 1] + arr[i]:
        if dp[-1] > dp[i - 1] + arr[i]:
            if tempMax < dp[-1]:
                tempMax = dp[-1]
        dp.append(dp[i - 1] + arr[i])
    else:
        if dp[-1] > tempMax:
            tempMax = dp[-1]
        dp.append(arr[i])

print(max(tempMax, dp[-1]))
