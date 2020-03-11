n = int(input())
arr = [[]for i in range(n + 1)]

for i in range(n):
    arr[i+1].append(int(input()))

answer = []


def dfs(v, i):
    checker[v] = True

    for k in arr[v]:
        if not checker[k]:
            dfs(k, i)
        elif checker[k] and k == i:
            answer.append(k)


for i in range(1, n + 1):
    checker = [False] * (n+1)
    dfs(i, i)

print(len(answer))
for i in range(len(answer)):
    print(answer[i])
