n = int(input())

answer = 0

for i in range(n):
    word = str(input())
    stack = []
    for j in word:
        if not stack:
            stack.append(j)
        else:
            if stack[-1] == j:
                stack.pop()
            else:
                stack.append(j)

    if not stack:
        answer += 1

print(answer)
