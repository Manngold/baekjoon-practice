num = str(input())
cars = list(map(str, input().split()))

cnt = 0

for i in cars:
    if num == i[-1]:
        cnt += 1

print(cnt)