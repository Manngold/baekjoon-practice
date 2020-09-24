n = int(input())

def lcm(i,j):
  while(j != 0):
    r = i % j
    i = j
    j = r

  return i

for _ in range(n):
  a, b = map(int, input().split())
  a, b = max(a, b), min(a,b)
  print(int(a*b / lcm(a,b)))

  

