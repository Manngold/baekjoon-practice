buger = []
beverage = []

for _ in range(3):
    buger.append(int(input()))

for _ in range(2):
    beverage.append(int(input()))

answer = min(buger) + min(beverage) - 50

print(answer)