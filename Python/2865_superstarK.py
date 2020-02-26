n, m, k = map(int, input().split())

arr = []
maxArr = [0] * (n + 1)

for _ in range(m):
    arr.append(list(map(float, input().split())))

for i in range(m):
    for j in range(0, 2*n, 2):
        idx = int(arr[i][j])
        if maxArr[idx] < arr[i][j + 1]:
            maxArr[idx] = arr[i][j + 1]
        else:
            continue

answer = 0
maxArr = sorted(maxArr)

for i in range(k):
    answer += maxArr.pop()

print("%.1f" % answer)
