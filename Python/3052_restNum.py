arr = []

for _ in range(10):
    arr.append(int(input()) % 42)

answer = len(set(arr))
print(answer)