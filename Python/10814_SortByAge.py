n = int(input())
arr = [[]for _ in range(201)]

for _ in range(n):
    i = list(map(str, input().split()))
    age = int(i[0])
    arr[age].append(i)

for i in arr:
    if i:
        for j in i:
            print(" ".join(j))
