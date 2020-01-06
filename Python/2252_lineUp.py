n, m = map(int, input().split())

q = []

cnt = [0] * n
compare = []
answer = []

for i in range(m):
    a, b = map(int, input().split())
    cnt[b-1] += 1
    compare.append([a, b])

for i in range(n):
    if cnt[i] == 0:
        q.append(i + 1)

while q:
    for i in q:
        temp = i
        q.remove(i)
        answer.append(temp)
        for j in range(len(compare)):
            a, b = compare[j][0], compare[j][1]
            cnt[b-1] -= 1
            if cnt[b-1] == 0:
                q.append(b)

print(answer)
