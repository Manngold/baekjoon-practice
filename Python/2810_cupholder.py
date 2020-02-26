n = int(input())
s = input()
cnt = 0

answer = 1

for i in s:
    if i == "S":
        answer += 1
    elif i == "L":
        if cnt == 1:
            answer += 1
            cnt = 0
        else:
            cnt += 1
            continue

if answer > n:
    print(n)
else:
    print(answer)
