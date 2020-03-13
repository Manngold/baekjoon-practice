n = int(input())

answer = 0

l = len(str(n))

if l == 1:
    answer += n
else:
    for i in range(1, l):
        answer += i * (9 * (10 ** (i - 1)))

if l > 1:
    rest = n - 10 ** (l-1) + 1
    answer += rest * l

print(answer)
