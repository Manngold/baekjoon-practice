n, m = map(int, input().split())
compare = []
studentList = [[] for i in range(n + 1)]
cnt = [0] * (n + 1)
q = []
answer = []

for i in range(m):
    l = list(map(int, input().split()))
    compare.append(l)

for [i, j] in compare:
    studentList[i].append(j)
    cnt[j] += 1

for i in range(1, n + 1):
    if cnt[i] == 0:
        q.append(i)

while q:
    for i in q:
        temp = i
        q.remove(i)
        answer.append(temp)
        for j in studentList[temp]:
            cnt[j] -= 1
            if cnt[j] == 0:
                q.append(j)

print(" ".join(map(str, answer)))
