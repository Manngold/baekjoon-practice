case = int(input())
password = []

for i in range(case):
    password.append(input())

opec = ["<", ">", "-"]
answers = []
stack = []
temp = []

for i in range(case):
    for s in password[i]:
        if s in opec:
            if s == "<":
                if len(stack) == 0:
                    continue
                else:
                    temp.append(stack.pop())
            elif s == ">":
                if len(temp) == 0:
                    continue
                else:
                    stack.append(temp.pop())
            else:
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
        else:
            stack.append(s)
    while len(temp) != 0:
        stack.append(temp.pop())
    answers.append(''.join(stack))
    stack = []

for i in answers:
    print(i)
    
