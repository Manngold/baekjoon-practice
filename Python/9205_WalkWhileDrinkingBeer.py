t = int(input())


def dfs(node):
    for i in range(node + 1, len(searchMap)):
        if searchMap[node][i] == 1 and visited[i] == False:
            visited[i] = True
            dfs(i)


for _ in range(t):
    n = int(input())
    coord = []

    for _ in range(2 + n):
        coord.append(list(map(int, input().split())))

    searchMap = [[0 for _ in range(2 + n)] for _ in range(2 + n)]
    visited = [False for _ in range(2 + n)]

    for i in range(len(coord)):
        node = coord[i]
        for j in range(len(coord)):
            x, y = coord[j]
            if i == j:
                continue
            else:
                if abs(node[0] - x) + abs(node[1] - y) <= 1000:
                    searchMap[i][j] = 1
                else:
                    continue

    visited[0] = True
    for i in range(1, len(searchMap)):
        if searchMap[0][i] == 1 and visited[i] == False:
            visited[i] = True
            dfs(i)

    if visited[-1] == True:
        print("happy")
    else:
        print("sad")
