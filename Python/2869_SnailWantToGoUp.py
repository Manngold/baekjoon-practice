a, b, v = map(int, input().split())

answer = (v - a) // (a - b)

if (v-a) % (a-b) > 0:
    answer += 2
else:
    answer += 1

print(answer)
