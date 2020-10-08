n, k = map(int, input().split())

arr = []
target = []

gold = []
silver = []
bronz = []

for _ in range(n):
  arr.append(list(map(int, input().split())))
  if arr[-1][0] == k:
    target = arr[-1]

for i in arr:
  if i == target:
    continue
  if i[1] > target[1]:
    if len(gold) == 0:
      gold.append(i)
    else:
      gold.append(i)
  elif i[1] == target[1]:
    if i[2] > target[2]:
      if len(silver) == 0:
        silver.append(i)
      else:
        silver.append(i)
    elif i[2] == target[2]:
      if i[3] > target[3]:
        if len(bronz) == 0:
          bronz.append(i)
        else:
          bronz.append(i)

print(len(gold)+len(silver)+len(bronz) + 1)
        
      



