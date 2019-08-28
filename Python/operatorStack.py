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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for c in S:
        if c == "(":
            opStack.push(c)
        else:
            if c == ")":
                while opStack.peek() != "(":
                    answer += opStack.pop()
                opStack.pop()
            else:
                if c in prec:
                    top = opStack.peek()
                    if prec[c] >= prec[top]:
                        answer += opStack.peek()
                        opStack.pop()
                        opStack.push(c)
                else:
                        answer += c
    while not opStack.isEmpty():
        answer += opStack.peek()
        opStack.pop()

    return answer