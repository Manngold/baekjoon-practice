from collections import deque

a = input()
t = deque(input())

mode = True
delMode = True
isExist = True

answer = deque()

while isExist:
    if mode:
        for _ in range(len(t)):
            answer.append(t.popleft())
            delMode = True
            if len(answer) >= len(a):
                for j in range(-1, (-len(a))-1, -1):
                    if answer[j] != a[j]:
                        mode = False
                        break
                if delMode:
                    for _ in range(len(a)):
                        answer.pop()

                for _ in range(len(answer)):
                    t.append(answer.pop())
                mode = False
                break

    else:
        for _ in range(len(t)):
            answer.appendleft(t.pop())
            delMode = True
            if len(answer) >= len(a):
                for j in range(-1, (-len(a)-1), -1):
                    if answer[j] != a[j]:
                        mode = False
                        break
                if delMode:
                    for _ in range(len(a)):
                        answer.pop()
                for _ in range(len(answer)):
                    t.append(answer.popleft())
                mode = True
                break

    if not a in "".join(t):
        isExist = False

print("".join(t))
