n, k = map(int, input().split())

arr = list(map(int, input().split()))

answer = 1

l = len(arr) - k

if l % (k - 1) != 0:
    answer += l // (k - 1) + 1
else:
    answer += l // (k - 1)

print(answer)
