from collections import deque

m, n, k = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(m)]
checker = [[False for _ in range(n)] for _ in range(m)]
answer = []

for _ in range(k):
  x0,y0,x1,y1 = map(int, input().split())
  for y in range(y0, y1):
    for x in range(x0, x1):
      if arr[y][x] == 0:
        arr[y][x] += 1
        checker[y][x] = True

def dfs(y, x):
  count = 0
  q = deque()
  q.append([x, y])

  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  while q:
    x, y = q.popleft()
    if checker[y][x] == False and arr[y][x] == 0:
      checker[y][x] = True
      arr[y][x] = 1
      count += 1
    else:
      continue
    for i in range(4):
      if x + dx[i] >= 0 and y + dy[i] >= 0 and x+dx[i] < n and y + dy[i] < m:
        if arr[y + dy[i]][x+dx[i]] == 0 and checker[y + dy[i]][x+dx[i]] == False:
          q.append([x+dx[i],y+dy[i]])
  return count

for y in range(m):
  for x in range(n):
    if arr[y][x] == 0 and checker[y][x] == False:
      answer.append(dfs(y, x))

print(len(answer))
print(" ".join(map(str, sorted(answer))))