n = int(input())

words = []

for _ in range(n):
    words.append(input())

answer = 0
checker = ""

for i in words:
    for j in i:
        if len(checker) == 0:
            checker += j
        else:
            if j in checker and checker[-1] == j:
                checker += j
            else:
                if not j in checker:
                    checker += j
                else:
                    break
    if checker == i:
        answer += 1
    checker = ""
print(answer)
