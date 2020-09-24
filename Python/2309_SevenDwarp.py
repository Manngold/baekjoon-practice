from itertools import combinations

arr=[]
for _ in range(9):
  arr.append(int(input()))

a = list(combinations(arr, 7))

for i in a:
  i = sorted(i)
  if sum(i) == 100:
    for j in i:
      print(j)
    break

