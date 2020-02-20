n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input())))

b = []
for i in range(n):
    b.append(list(map(int, input())))

answer = 0

for i in range(n-2):
    if n < 3 or m < 3:
        break
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            for k in range(i, i+3):
                for t in range(j, j + 3):
                    a[k][t] = 1 - a[k][t]
            answer += 1

if a == b:
    print(answer)
else:
    print(-1)
