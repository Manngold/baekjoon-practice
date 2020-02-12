n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input())))

b = []
for i in range(n):
    b.append(list(map(int, input())))

answer = 0

for i in range(n):
    if n <= 3 or m <= 3:
        break
    for j in range(m):
        if a[i][j] != b[i][j]:
            for k in range(i, i+3):
                if k >= n:
                    continue
                for t in range(j, j + 3):
                    if t >= m:
                        continue
                    a[k][t] = b[k][t]
            answer += 1
        else:
            continue

if n < 3 or m < 3:
    if not a == b:
        print(-1)
    else:
        print(0)
elif n == 3 and m == 3:
    if not a == b:
        print(1)
    else:
        print(answer)
else:
    print(answer)
