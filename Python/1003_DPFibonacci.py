n = int(input())


for _ in range(n):
    dp = [[1, 0], [0, 1], [1, 1]]
    t = int(input())
    if t < 3:
        answer = dp[t]
        print(answer[0], answer[1])
        continue
    else:
        for i in range(3, t + 1):
            dp.append([dp[-2][0]+dp[-1][0], dp[-2][1]+dp[-1][1]])

    answer = dp[-1]
    print(answer[0], answer[1])
