towers = int(input())
levels = list(map(int,input().split()))
answers = []
stack = []

for i in range(towers):
    if i == 0:
        answers.append(0)
        stack.append(i)
        continue
    if levels[i] > levels[stack[-1]]:
        while len(stack) != 0:
            if levels[i] > levels[stack[-1]]:
                stack.pop()
                continue
            if levels[i] <= levels[stack[-1]]:
                answers.append(stack[-1] + 1)
                stack.append(i)
                break
        if len(stack) == 0:
            answers.append(0)
            stack.append(i)
            continue
    if levels[i] <= levels[stack[-1]] and len(answers) == i:
        answers.append(stack[-1] + 1)
        stack.append(i)
        continue

print(" ".join(map(str, answers)))

    
    
    




    


