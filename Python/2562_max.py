arr = []
cnt = 1

for _ in range(9):
    arr.append(int(input()))

for i in arr:
    if i == max(arr):
        print(max(arr))
        print(cnt)
    else:
        cnt += 1
        continue



