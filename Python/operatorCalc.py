class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for c in tokenList:
        if c == "(":
            opStack.push(c)
        else:
            if c == ")":
                while opStack.peek() != "(":
                    postfixList.append(opStack.pop())
                opStack.pop()
            else:
                if c in prec:
                    if opStack.isEmpty():
                        opStack.push(c)
                    else:
                        if prec[c] > prec[opStack.peek()]:
                            opStack.push(c)
                        else:
                            postfixList.append(opStack.pop())
                            opStack.push(c)
                else:
                    postfixList.append(c)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    totalStack = []
    left = 0
    right = 0
    for i in tokenList:
        if type(i) == int:
            totalStack.append(i)
        else:
            right = totalStack.pop()
            left = totalStack.pop()
            if i == "+":
                totalStack.append(left + right)
            elif i == "-":
                totalStack.append(left - right)
            elif i == "*":
                totalStack.append(left * right)
            else:
                totalStack.append(left / right)
    return totalStack.pop()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val