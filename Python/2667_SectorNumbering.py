from collections import deque

n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
checker = [[False for _ in range(n)] for _ in range(n)]
sector = 0
house = []

for i in range(n):
    row = input()
    for j in range(n):
        arr[i][j] = int(row[j])


def dfs(y, x):

    q = deque()
    q.append([y, x])
    houseNum = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:

        y, x = q.popleft()
        houseNum += 1
        checker[y][x] = True

        for i in range(4):
            if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= n:
                continue
            if checker[y + dy[i]][x + dx[i]] == False and arr[y + dy[i]][x + dx[i]] == 1:
                if not [y + dy[i], x + dx[i]] in q:
                    q.append([y + dy[i], x+dx[i]])
                else:
                    continue
            else:
                continue

    house.append(houseNum)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            if checker[i][j] == True:
                continue
            sector += 1
            dfs(i, j)
        else:
            continue

house = sorted(house)
print(sector)
for i in range(len(house)):
    print(house[i])
