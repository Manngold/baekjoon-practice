n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(str, input().split())))
  arr[i][1] = int(arr[i][1])
  arr[i][2] = int(arr[i][2])
  arr[i][3] = int(arr[i][3])

arr = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in arr:
  print(i[0])