subjects = int(input())
score = list(map(float, input().split()))

m = max(score)

for i in range(subjects):
    score[i] = score[i] / m * 100

print(round(sum(score) / float(subjects), 6))

