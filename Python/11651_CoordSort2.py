n = int(input())

arr = []

for _ in range(n):
  x, y = map(int, input().split())
  arr.append([x, y])

for i in sorted(arr, key=lambda i: (i[1], i[0])):
  print(i[0], i[1])
