n, m = map(int, input().split())

line = []

for i in range(m):
    a, b = map(int, input().split())
    if not a in line and b in line:
        storage = []
        for j in range(len(line)):
            if line[j] == b:
                storage = line[j:]
                line = line[:j]
                line.append(a)
                line += storage
                break
            else:
                continue
    elif a in line and not b in line:
        storage = []
        for j in range(len(line)):
            if line[j] == a:
                storage = line[a+1:]
                line = line[:a+1]
                line.append(b)
                line += storage
                break
            else:
                continue
    else:
        line.append(a)
        line.append(b)

print(line)
