s = input()
boom = input()

answer = []

for i in s:
    answer.append(i)

    mode = True

    if len(answer) >= len(boom):
        for j in range(-1, (-len(boom))-1, -1):
            if answer[j] != boom[j]:
                mode = False
                break

        if mode:
            for _ in range(len(boom)):
                answer.pop()

if len(answer) == 0:
    print("FRULA")
else:
    print("".join(answer))
