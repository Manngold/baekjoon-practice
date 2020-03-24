brakect = ["(", ")", "[", "]"]

while True:
    answer = ""
    text = input()
    if text == ".":
        break
    else:
        stack = []
        for i in text:
            if not i in brakect:
                continue
            else:
                if i == ")":
                    if not stack:
                        answer = "no"
                        break
                    else:
                        if not stack[-1] == "(":
                            answer = "no"
                            break
                        else:
                            stack.pop()
                elif i == "]":
                    if not stack:
                        answer = "no"
                        break
                    else:
                        if not stack[-1] == "[":
                            answer = "no"
                            break
                        else:
                            stack.pop()
                else:
                    stack.append(i)
        if not stack and not answer == "no":
            answer = "yes"
            print(answer)
        else:
            answer = "no"
            print(answer)
