from collections import deque
from itertools import combinations

l, c = map(int, input().split())

c = deque(sorted(list(map(str, input().split()))))
aeiou = "aeiou"
answers = [];

def checker(word):
  isValid = False
  for i in word:
    if i in aeiou:
      isValid = True
  return isValid

for i in range(len(c) - l + 1):
  t = ""
  t += c.popleft()
  comb = list(combinations(c, l - 1))
  for j in comb:
    answer = t + "".join(sorted(list(j)))
    if answer in answers:
      continue
    else:
      if checker(answer):
        answers.append(answer)

for i in answers:
  print(i)
  
    

