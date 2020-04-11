import sys

rope = int(input())

answer = 0
info = []

for _ in range(rope):
    info.append(int(input()))

info = sorted(info, reverse=True)

for i in range(rope):
    weight = info[i] * (i + 1)
    if answer < weight:
        answer = weight

print(answer)
