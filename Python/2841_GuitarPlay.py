stack = [[] for _ in range(7)]

answer = 0
n, p = map(int, input().split())

for _ in range(n):
    string, flat = map(int, input().split())
    if not stack[string]:
        stack[string].append(flat)
        answer += 1
    else:
        if stack[string][-1] < flat:
            stack[string].append(flat)
            answer += 1
        elif stack[string][-1] == flat:
            continue
        else:
            while stack[string][-1] > flat:
                stack[string].pop()
                answer += 1
                if not stack[string]:
                    break
            if stack[string]:
                if stack[string][-1] == flat:
                    continue
            stack[string].append(flat)
            answer += 1

print(answer)
