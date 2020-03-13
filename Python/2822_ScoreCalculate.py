score = []

total = 0
solveNum = []

for _ in range(8):
    score.append(int(input()))

for i in range(5):
    total += sorted(score, reverse=True)[i]
    solveNum.append(str(score.index(sorted(score, reverse=True)[i]) + 1))

print(total)
print(" ".join(sorted(solveNum)))
