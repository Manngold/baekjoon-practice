import math
from collections import deque
n = int(input())

arr = []

for _ in range(n):
  t = int(input())
  if not arr:
    arr.append(t)
  else:
    q = deque()
    while(arr):
      if arr[-1] <= t:
        arr.append(t)
        break
      else:
        q.appendleft(arr.pop())
    if q and not arr:
      arr.append(t)

    arr = arr + list(q)
  if len(arr) % 2:
    print(arr[len(arr) // 2])
  else:
    print(min(arr[len(arr) // 2], arr[len(arr) // 2 - 1]))



    