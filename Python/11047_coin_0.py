spec = list(map(int,input().split()))
money = []
num = spec[0]
target = spec[1]
coin = 0

for i in range(spec[0]):
    money.append(int(input()))

while target != 0:
    if target < money[-1]:
        money.pop()
        continue
    elif target >= money[-1]:
        coin += target // money[-1]
        target = target % money[-1]
        continue

print(coin)