from collections import deque

t = int(input())


def dfs(y, x, farm, checker):

    q = deque()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q.append([y, x])

    while q:
        y, x = q.popleft()
        checker[y][x] = True

        for i in range(4):
            if x + dx[i] < 0 or x + dx[i] >= m or y + dy[i] < 0 or y + dy[i] >= n:
                continue
            if checker[y + dy[i]][x + dx[i]] == False and farm[y + dy[i]][x + dx[i]] == 1:
                if not [y+dy[i], x + dx[i]] in q:
                    q.append([y+dy[i], x + dx[i]])
                else:
                    continue
            else:
                continue
    return checker


for _ in range(t):
    m, n, k = map(int, input().split())
    answer = 0

    farm = [[0 for _ in range(m)] for _ in range(n)]
    checker = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                if checker[i][j] == True:
                    continue
                checker = dfs(i, j, farm, checker)
                answer += 1
            else:
                continue
    print(answer)
