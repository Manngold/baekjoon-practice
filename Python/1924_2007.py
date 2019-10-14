m, d = map(int, input().split())

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
dayCount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

totalDayCount = d
if m == 1:
    pass
else:
    for i in range(m-1):
        totalDayCount += dayCount[i]

rest = totalDayCount % 7

print(days[rest - 1])



