n = int(input())

case = [1, 2, 4]
for i in range(3, 10):
    case.append(case[i - 3] + case[i - 2] + case[i - 1])

for _ in range(n):
    t = int(input())
    print(case[t-1])
