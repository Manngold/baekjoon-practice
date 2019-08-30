length = int(input())
i = 0
arr = []

while i < length:
    data = input()
    arr.append(data)
    i += 1

psStack = []
answer = []
i = 0

while i < length:
    for c in arr[i]:
        if c == "(":
            psStack.append(c)
        else:
            if len(psStack) == 0:
                answer.append("NO")
                break
            else:
                psStack.pop()
                
    if len(answer) == i:
        if len(psStack) == 0:
            answer.append("YES")
        else:
            answer.append("NO")

    psStack = []
    i += 1

for a in answer:
    print(a)







    
    
        

        
