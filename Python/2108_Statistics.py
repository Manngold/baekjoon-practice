from operator import itemgetter
n = int(input())

dic = {}

for _ in range(n):
  i = int(input())
  if not i in dic:
    dic[i] = 1
  else:
    dic[i] += 1

s = []
for i in sorted(dic):
  for _ in range(dic[i]):
    s.append(i)
m = max(dic.values())
preq = []
for i in dic:
  if dic[i] == m:
    preq.append(i)
preq = sorted(preq)
print(round(sum(s) / n))
print(s[len(s) // 2])
if len(preq) >= 2:
  print(preq[1])
else:
  print(preq[-1])
print(s[len(s) - 1] - s[0])