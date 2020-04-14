nums = []

n, m = map(int, input().split())

for _ in range(n):
    nums.append(list(map(int, input())))

MAX = min(n, m)
answer = 0

for i in range(n):
    for j in range(m):
        for k in range(MAX):
            if i + k < n and j + k < m:
                if nums[i][j] == nums[i][j+k] and nums[i][j] == nums[i+k][j] and nums[i][j] == nums[i+k][j+k]:
                    if answer < k:
                        answer = k
print((answer + 1) * (answer + 1))
