string = str(input())

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", "OPERATOR"]

answer = 0

for i in string:
    sec = 3
    for j in range(len(dial)):
        if i in dial[j]:
            answer += sec
            break
        else:
            sec += 1
            continue

print(answer)
