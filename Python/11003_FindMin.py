from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))

q = deque()
answers = []

for i in range(l):

    while q and a[i] <= a[q[-1]]:
        q.pop()

    q.append(i)
    answers.append(a[q[0]])

for i in range(l, len(a)):

    while q and q[0] <= i-l:
        q.popleft()

    while q and a[i] <= a[q[-1]]:
        q.pop()

    q.append(i)

    answers.append(a[q[0]])

for i in range(len(answers)):
    print(answers[i], end=' ')
