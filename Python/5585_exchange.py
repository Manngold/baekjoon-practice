money = 1000 - int(input())
coin = [1, 5, 10, 50, 100, 500]
answer = 0

while money != 0:
    if money // coin[-1] == 0:
        coin.pop()
        continue

    if money // coin[-1] != 0:
        answer += money // coin[-1]
        money = money % coin[-1]
        continue

print(answer)
