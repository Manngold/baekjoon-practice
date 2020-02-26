n = int(input())

arr = [[]] * n
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[i].append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i):
        if j == 0:
            dp[i-1][j] = arr[i][j] + arr[i-1][j]
            print(dp)
        elif j == i:
            dp[i-1][j] = arr[i][j] + arr[i-1][j-1]
            print(dp)
        else:
            if arr[i][j] + arr[i-1][j] > dp[i-1][j]:
                dp[i-1][j] = arr[i][j] + arr[i-1][j]
            if arr[i][j] + arr[i-1][j-1] > dp[i-1][j]:
                dp[i-1][j] = arr[i][j] + arr[i-1][j-1]
            else:
                continue
print(dp)
