a, b = map(str, input().split())

case = len(b) - len(a) + 1

answers = [0] * case

for i in range(0, case):
    slicedB = b[i:]
    for j in range(len(a)):
        if a[j] != slicedB[j]:
            answers[i] += 1
        else:
            continue

print(min(answers))
