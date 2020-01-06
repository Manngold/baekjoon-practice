n, m = map(int, input().split())

dna = []
totalDna = ""
totalDist = 0

for i in range(n):
    dna.append(str(input()))


def maxDna(t, g, a, c):
    if max(t, g, a, c) == a:
        return "A"
    elif max(t, g, a, c) == c:
        return "C"
    elif max(t, g, a, c) == g:
        return "G"
    else:
        return "T"


for i in range(m):
    t, a, g, c = 0, 0, 0, 0
    for j in range(n):
        if dna[j][i] == "T":
            t += 1
        elif dna[j][i] == "G":
            g += 1
        elif dna[j][i] == "A":
            a += 1
        else:
            c += 1
    totalDna += maxDna(t, g, a, c)
    totalDist += n - max(t, a, g, c)

print(totalDna)
print(totalDist)
