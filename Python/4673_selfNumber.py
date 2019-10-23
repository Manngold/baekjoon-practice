selfNumber = []
for i in range(1, 10001):
    result = i
    n = str(i)
    for j in n:
        result += int(j)
    selfNumber.append(result)

for i in range(1, 10001):
    if not i in selfNumber:
        print(i)