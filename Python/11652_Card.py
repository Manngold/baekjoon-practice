n = int(input())

answers = []
dic = {}

for _ in range(n):
  i = int(input())
  if not i in dic:
    dic[i] = 1
  else:
    dic[i] += 1

m = max(dic.values())

for i in dic:
  if dic[i] == m:
    answers.append(i)

print(min(answers))