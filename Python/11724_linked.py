def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

N, M = map(int, input().split())
adj = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for i in range(M):
    vertex = list(map(int, input().split()))
    adj[vertex[0]].append(vertex[1])
    adj[vertex[1]].append(vertex[0])

for i in range(1, len(visited)):
    if not(visited[i]):
        cnt += 1
        dfs(i)

print(cnt)