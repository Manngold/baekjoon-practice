t = int(input())
ox = []
score = []
cnt = 0

for _ in range(t):
    ox.append(str(input()))

for i in ox:
    for j in i:
        if j == "O":
            cnt += 1
            score.append(cnt)
            continue
        else:
            cnt = 0
            score.append(cnt)
    print(sum(score))
    score = []
    cnt = 0

