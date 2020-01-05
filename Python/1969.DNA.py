n, m = map(int, input().split())

dna = []
totalDist = 0

for i in range(n):
    dna.append(str(input()))

for i in range(m):
    cnt = {
        "T": 0,
        "A": 0,
        "G": 0,
        "C": 0
    }
    dist = 0
    for j in range(n):
        cnt[dna[j][i]] += 1
    for i in cnt:
        if cnt[i] > 0:
            dist += 1
        else:
            continue
    totalDist += dist - 1

print(totalDist)
