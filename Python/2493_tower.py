towers = int(input())
levels = list(map(int,input().split()))
answers = []
idx = 1

for i in range(towers):
    if i == 0:
        answers.append(0)
        idx = 1
        continue
    elif i == 1:
        if levels[i] <= levels[i - idx]:
            answers.append(i - idx + 1)
            idx = 1
            continue
        else:
            answers.append(0)
            idx = 1
            continue
    while levels[i] > levels[i - idx]:
        if idx == i:
            idx = 1
            answers.append(0)
            break
        idx += 1

    answers.append(i - idx + 1)
    idx = 1

print(" ".join(map(str, answers)))

    
    
    




    


