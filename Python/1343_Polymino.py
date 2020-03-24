n = input()

cnt = 0
answer = ""

for i in n:
    if i == "X":
        cnt += 1
    elif i == ".":
        if not cnt % 2 == 0:
            answer = -1
            break
        else:
            if cnt == 2:
                answer += "BB."
                cnt = 0
            elif cnt == 0:
                answer += "."
                continue
            else:
                answer += "AAAA" * (cnt // 4)
                answer += "B" * (cnt % 4)
                answer += "."
                cnt = 0

if cnt % 2 == 0:
    answer += "AAAA" * (cnt // 4)
    answer += "B" * (cnt % 4)
    cnt = 0
else:
    answer = -1


print(answer)
