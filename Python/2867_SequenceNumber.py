n = int(input())

l = []
idx = 0
answer = 0

for _ in range(n):
    l.append(int(input()))

for i in range(2, n + 1):
    while idx + i <= n:
        splitted = l[idx: idx + i]
        answer += max(splitted) - min(splitted)
        idx += 1
    idx = 0

print(answer)
