n = int(input())

arr = []

answer = 0

baseTemp = 0

for _ in range(n):
    height = int(input())
    if not height == 0:
        baseTemp += 1
    else:
        if answer < baseTemp:
            answer = baseTemp
        baseTemp = 0
    arr.append(height)

if answer < baseTemp:
    answer = baseTemp

stack = []

for i in arr:
    if not stack:
        stack.append(i)
    else:
        if i >= stack[-1]:
            stack.append(i)
        else:
            temp = 0
            tempStack = []
            while stack:
                tempStack.append(stack.pop())
                width = min(tempStack) * len(tempStack)
                if temp <= width:
                    temp = width
                else:
                    break

            if temp > answer:
                answer = temp
                stack = []
                stack.append(i)

if stack:
    temp = 0
    tempStack = []
    while stack:
        tempStack.append(stack.pop())
        width = min(tempStack) * len(tempStack)
        if temp <= width:
            temp = width
        else:
            break

    if temp > answer:
        answer = temp


print(answer)
