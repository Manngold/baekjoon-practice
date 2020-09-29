n = int(input())

arr = [[]for _ in range(51)]

for _ in range(n):
  word = input()
  l = len(word)
  arr[l].append(word)

for i in arr:
  if len(i) == 0:
    continue
  else:
    for j in set(sorted(i)):
      print(j)