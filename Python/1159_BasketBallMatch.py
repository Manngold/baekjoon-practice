n = int(input())
starting = {}

for _ in range(n):
    name = input()
    firstName = name[0]
    if not firstName in starting:
        starting[firstName] = 1
    else:
        starting[firstName] += 1

answer = ""

for i in starting:
    if starting[i] >= 5:
        answer += i
answer = sorted(answer)

if len(answer) == 0:
    print("PREDAJA")
else:
    print("".join(answer))
