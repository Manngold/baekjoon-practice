case = int(input())
answer = 0
for _ in range(case):
    n, m = map(int, input().split())
    book = [1] * (n + 1)
    order = []
    for i in range(m):
        order.append(list(map(int, input().split())))
    order.sort(key=lambda x: x[1])
    for i in order:
        a, b = map(int, i)
        for j in range(a, b + 1):
            if book[j] == 1:
                book[j] -= 1
                answer += 1
                break
print(answer)
