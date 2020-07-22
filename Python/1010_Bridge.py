t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    answer = 1
    k = n - m

    for i in range(k+1, n+1):
        answer *= i
    for i in range(1, m+1):
        answer = answer // i

    print(answer)
