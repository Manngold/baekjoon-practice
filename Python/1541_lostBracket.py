a = str(input())

equation = []
nums = ""
mode = False

opers = ["+", "-"]

for i in a:
    if not i in opers:
        nums += i
    else:
        equation.append(int(nums))
        equation.append(i)
        nums = ""

equation.append(int(nums))

answer = 0
storage = 0

for i in equation:
    if not i in opers and not mode:
        answer += i
        continue
    if i == "-":
        mode = True
    if not i in opers and mode:
        answer -= i

print(answer)
