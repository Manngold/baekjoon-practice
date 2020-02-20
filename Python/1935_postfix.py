n = int(input())

equation = list(input())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = []

oper = ["+", "-", "*", "/"]

for _ in range(n):
    num.append(float(input()))

stack = []

for i in range(len(equation)):
    if equation[i] in alphabet:
        equation[i] = num[alphabet.find(equation[i])]


def calculator(left, right, oper):
    if oper == "+":
        return left + right
    elif oper == "-":
        return left - right
    elif oper == "*":
        return left * right
    elif oper == "/":
        return left / right


for i in equation:
    if not stack:
        stack.append(i)
    else:
        if i in oper:
            right = stack.pop()
            left = stack.pop()
            stack.append(calculator(left, right, i))

        else:
            stack.append(i)

print("%.2f" % stack[0])
