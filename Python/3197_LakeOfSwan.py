import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
lake = []
cnt = 0
swan1 = []
swan2 = []

for _ in range(r):
  arr = list(sys.stdin.readline().replace("\n", ""))
  lake.append(arr)

def melting(lake):
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  for y in range(r):
    for x in range(c):
      if lake[y][x] == "X":
        for i in range(4):
          if y + dy[i] >= 0 and x + dx[i] >= 0 and x + dx[i] < c and y + dy[i] < r:
            if lake[y+dy[i]][x+dx[i]] == "." or lake[y+dy[i]][x+dx[i]] == "L":
              lake[y][x] = "*"
              break
  for y in range(r):
    for x in range(c):
      if lake[y][x] == "*":
        lake[y][x] = "."
  return lake

def makeChecker(lake):
  checker = []
  for y in range(r):
    arr = []
    for x in range(c):
      if lake[y][x] == "." or lake[y][x] == "L":
        if len(swan1) < 2 and lake[y][x] == "L":
          swan1.append(y)
          swan1.append(x)
        elif len(swan2) < 2 and lake[y][x] == "L":
          swan2.append(y)
          swan2.append(x)
        arr.append(False)
      elif lake[y][x] == "X":
        arr.append(True)
    checker.append(arr)
  return checker

def dfs(lake):
  visited = makeChecker(lake)
  q = deque()
  q.append(swan1)
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  while q:
    y, x = q.popleft()
    visited[y][x] = True

    for i in range(4):
      if y + dy[i] >= 0 and x + dx[i] >= 0 and x + dx[i] < c and y + dy[i] < r:
        if visited[y + dy[i]][x + dx[i]] == False:
                if not [y+dy[i], x + dx[i]] in q:
                    q.append([y+dy[i], x + dx[i]])
  if visited[swan2[0]][swan2[1]]:
    return True
  else:
    return False

while True:
  isValid = dfs(lake)
  if isValid:
    print(cnt)
    break
  else:
    lake = melting(lake)
    cnt += 1



