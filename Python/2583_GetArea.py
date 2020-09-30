from collections import deque

m, n, k = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(m)]
answer = []

for _ in range(k):
  x0,y0,x1,y1 = map(int, input().split())
  for y in range(y0, y1):
    for x in range(x0, x1):
      if arr[y][x] == 0:
        arr[y][x] += 1

def dfs(arr, x, y):
  cnt = 0
  q = deque()
  q.append([x,y])

  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  while q:
    x, y = q.popleft()
    print(y, x)
    cnt += 1
    arr[y][x] = 1

    for i in range(4):
      if y + dy[i] > 0 and x + dx[i] > 0 and x + dx[i] < n and y + dy[i] < m:
        if arr[y + dy[i]][x + dx[i]] == 0:
          q.append([y+dy[i], x+dx[i]])

  return cnt

for i in range(m):
  for j in range(n):
    if arr[i][j] == 0:
      answer.append(dfs(arr, j, i))

print(answer)

# [
#   [0, 0, 0, 0, 1, 1, 0],
#   [0, 1, 0, 0, 1, 1, 0],
#   [1, 1, 1, 1, 0, 0, 0],
#   [1, 1, 1, 1, 0, 0, 0],
#   [0, 1, 0, 0, 0, 0, 0]
#   ]