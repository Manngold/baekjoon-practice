from collections import deque

t = int(input())


def bfs(idx):
    if idx == len(searchMap) - 1:
        return "happy"
    else:
        for i in range(idx + 1, len(searchMap)):
            if searchMap[idx][i] == 1 and visited[i] == False:
                visited[i] = True
                bfs(i)


for _ in range(t):
    n = int(input())
    coord = []
    for _ in range(2 + n):
        coord.append(list(map(int, input().split())))
    answer = ""
    searchMap = [[0 for _ in range(2 + n)] for _ in range(2 + n)]
    visited = [False for _ in range(2 + n)]

    for i in range(len(coord)):
        point = coord[i]
        for j in range(len(coord)):
            x, y = coord[j]
            if i == j:
                continue
            else:
                if x - point[0] + y - point[1] <= 1000:
                    searchMap[i][j] = 1
                else:
                    continue

    visited[0] = True

    for i in range(len(searchMap)):
        if searchMap[0][i] == 1:
            answer = bfs(i)

    if answer == None:
        answer = "sad"

    print(answer)
