scores = []
total = 0

for _ in range(5):
    a = int(input())
    if a < 40:
        a = 40
    scores.append(a)
    
for i in scores:
    total += i

print(total // 5)