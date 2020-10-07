n, k = map(int, input().split())
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

arr = sorted(arr, key = lambda x: (-x[1],-x[2],-x[3]))

rank = []

for i in arr:
  if len(rank) == 0:
    rank.append(i)
  else:
    if rank[-1][1:4] == i[1:4]:
      rank[-1] += i
    else:
      rank.append(i)

for i in range(len(rank)):
  if len(rank[i]) == 4:
    if rank[i][0] == k:
      print(i+1)
      break
  else:
    for j in range(0,len(rank[i]),4):
      if rank[i][j] == k:
        print(i + 1)
        break

