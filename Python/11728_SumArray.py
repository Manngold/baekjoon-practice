from collections import deque
n,m = map(int, input().split())
a = deque(map(int, input().split()))
b = deque(map(int, input().split()))

answer = []

for _ in range(n + m):
  if len(a) == 0:
    while(b):
      answer.append(str(b.popleft()))
      break
  
  elif len(b) == 0:
    while(a):
      answer.append(str(a.popleft()))
      break
  
  else:
    if a[0] > b[0]:
      answer.append(str(b.popleft()))
    else:
      answer.append(str(a.popleft()))
  
  if len(a) == 0 and len(b) == 0:
    break

print(" ".join(answer))