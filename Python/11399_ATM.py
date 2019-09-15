people = int(input())
time = list(map(int,input().split()))
time.sort()
answer = 0

for i in range(people):
    total = 0
    for j in range(i+1):
        total += time[j]
    answer += total

print(answer)
