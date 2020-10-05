n = int(input())
dic = {}
arr = list(map(int, input().split()))
for i in arr:
  dic[i] = 1

m = int(input())
arr2 = list(map(int, input().split()))
answer = []

for i in arr2:
  if i in dic:
    answer.append('1')
  else:
    answer.append('0')

print(" ".join(answer))
