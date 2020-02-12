n = int(input())
origin = list(map(int, input().split()))
goal = list(map(int, input().split()))
answer = 0

arr = [0]*n

for i in range(n):
    arr[i] = goal[i] - origin[i]

stack = []
while not arr == [0]*n:
    for _ in range(n):
        if not stack:
            stack.append(arr.pop())
        else:
            if arr[-1] > 0:
                if stack[-1] >= 0:
                    stack.append(arr.pop())
                else:
                    break
            elif arr[-1] < 0:
                if stack[-1] <= 0:
                    stack.append(arr.pop())
                else:
                    break
            else:
                if stack[-1] == 0:
                    stack.append(arr.pop())
                else:
                    break
    if stack[-1] > 0:
        for i in range(len(stack)):
            if stack[i] == 0:
                continue
            else:
                stack[i] -= 1
    else:
        for i in range(len(stack)):
            if stack[i] == 0:
                continue
            else:
                stack[i] += 1
    while stack:
        arr.append(stack.pop())

    answer += 1

print(answer)
