n = int(input())

timetable = []

answer = []

for _ in range(n):
    timetable.append(list(map(int, input().split())))

timetable = sorted(timetable, key=lambda x: (x[1], x[0]))
answer.append(timetable[0])

print(timetable)

for i in range(1, n):
    if timetable[i][0] < answer[-1][1]:
        continue
    else:
        answer.append(timetable[i])

print(len(answer))
