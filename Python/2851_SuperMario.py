mushroom = []

for _ in range(10):
    mushroom.append(int(input()))

answer = 0

for score in mushroom:
    new = answer + score
    old = answer
    if abs(100 - new) <= abs(100 - old):
        answer = new
    else:
        answer = old
        break

print(answer)
