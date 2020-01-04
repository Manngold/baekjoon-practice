n, m = map(int, input().split())

dna = []

for i in range(n):
    dna.append(list(input()))

cutDna = []
trimedData = []
for i in range(m):
    for j in range(n):
        cutDna.append(dna[j][i])
    trimedData.append(cutDna)
    cutDna = []

dist = 0
minDna = ""

for i in trimedData:

    dist += len(set(i)) - 1

print(dist)
