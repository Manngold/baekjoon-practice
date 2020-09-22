n, b = map(int, input().split())
a = []

for _ in range(n):
  a.append(list(map(int,input().split())))

def matrixSquare(a, b):
  if b == 1:
    for i in range(n):
      for j in range(n):
        a[i][j] %= 1000
    return a
  elif b%2 == 1:
    temp = [[0 for _ in range(n)] for _ in range(n)]
    c = matrixSquare(a, b - 1)
    for i in range(n):
      for j in range(n):
        for k in range(n):
          temp[i][j]+= c[i][k] *a[k][j]
        temp[i][j] %= 1000
    return temp
  else:
    tmp=[[0 for _ in range(n)] for _ in range(n)]
    c=matrixSquare(a,b//2)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[i][j]+=c[i][k]*c[k][j]
            tmp[i][j]%=1000
    return tmp

result = matrixSquare(a, b)
for li in result:
    for p in li:
        print(p,end=' ')
    print()


