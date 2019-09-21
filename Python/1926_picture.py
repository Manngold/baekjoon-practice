from collections import deque

q = deque()

h, w = map(int, input().split())

picture = []
visited = []

picsizes = []

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for _ in range(h):
    picture.append(list(map(int, input().split())))
    visited.append([False]*w)

def bfs(y, x):
    size = 0
    q.append([y, x])
    while q:
        y,x = q.popleft()
        visited[y][x] = True
        size += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < w and ny >= 0 and ny < h:
                if picture[ny][nx] == 1 and visited[ny][nx] == False and not [ny, nx] in q:
                    q.append([ny, nx])
                nx -= dx[i]
                ny -= dy[i]

    picsizes.append(size)

for y in range(h):
    for x in range(w):
        if picture[y][x] == 1 and visited[y][x] == False:
            bfs(y,x)




print(len(picsizes))
if len(picsizes) == 0:
    print(0)
else:
    print(max(picsizes))