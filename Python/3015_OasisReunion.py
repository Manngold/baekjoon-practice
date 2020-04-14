n = int(input())

answer = 0
stack = []

for _ in range(n):
    h = int(input())

    while stack and stack[-1][0] < h:

        answer += stack.pop()[1]

    if stack and stack[-1][0] == h:

        cnt = stack.pop()[1]
        answer += cnt

        if len(stack) != 0:
            answer += 1

        stack.append((h, cnt+1))
    else:
        if len(stack) != 0:
            answer += 1

        stack.append((h, 1))

print(answer)
