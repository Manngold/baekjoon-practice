n = list(input())

m = int(input())

stack = []

for _ in range(m):
  command = input()
  if command[0] == "L":
    if len(n) != 0:
      stack.append(n.pop())
  if command[0] == "D":
    if len(stack) != 0:
      n.append(stack.pop())
  if command[0] == "B":
    if len(n) != 0:
      n.pop()
  if command[0] == "P":
    n.append(command[2])

while(stack):
  n.append(stack.pop())  
  
print("".join(n))