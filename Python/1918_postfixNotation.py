a = input()

opStack = []
answer = ""
opec = {
    "*" : 3,
    "/" : 3,
    "+" : 2,
    "-" : 2,
    "(" : 1,
    ")" : 1
}

for i in a:
    if i in opec:
        if i == "(":
            opStack.append(i)
        elif i == ")":
            while opStack[-1] != "(":
                answer += opStack.pop()
            opStack.pop()
        else:
            if len(opStack) != 0:
                if opec[i] > opec[opStack[-1]]:
                    opStack.append(i)
                else:
                    while opec[i] <= opec[opStack[-1]]:
                        answer += opStack.pop()
                        if len(opStack) == 0:
                            break
                    opStack.append(i)
            else:
                opStack.append(i)
    else:
        answer += i
        
while len(opStack) != 0:
    answer += opStack.pop()

print(answer)