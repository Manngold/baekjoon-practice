n = int(input())

dic = {}
arr = list(map(int, input().split()))

for i in arr:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

for i in sorted(dic.keys()):
  print(i, end=" ")