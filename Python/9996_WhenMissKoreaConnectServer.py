n = int(input())

pattern = input()

words = []

answer = []

for i in range(n):
    words.append(input())

front = []
back = []
frontMode = True

for i in pattern:
    if frontMode and not i == "*":
        front.append(i)
    elif not frontMode and not i == "*":
        back.append(i)
    else:
        frontMode = False

for i in range(n):
    word = words[i]
    f = "".join(front)
    b = "".join(back)
    if word[:len(front)] == f and word[len(word) - len(back):] == b:
        if len(f) + len(b) > len(word):
            answer.append("NE")
            continue
        answer.append("DA")
    else:
        answer.append("NE")

for i in range(len(answer)):
    print(answer[i])
