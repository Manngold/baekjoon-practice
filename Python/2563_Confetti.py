n = int(input())

whiteBoard = [[0 for _ in range(101)] for _ in range(101)]
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if whiteBoard[i][j] == 1:
                continue
            else:
                whiteBoard[i][j] = 1
                answer += 1

print(answer)
