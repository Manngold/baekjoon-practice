while True:
  answer = 'yes'
  n = input()
  l = len(n)

  if n == '0':
    break
  
  stack = []
  
  for i in range(l // 2):
    stack.append(n[i])
    
  if l % 2 == 0:
    s = l // 2
  else:
    s = (l // 2) + 1  

  for i in range(s, l):
    if stack.pop() != n[i]:
      answer = 'no'
      break
  print(answer)