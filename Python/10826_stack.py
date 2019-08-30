commands = int(input())
i = 0
cmdStack = []
arr = []
while i < commands:

    cmd = input()
    cmdStack.append(cmd)
    i += 1

i = 0

while i < len(cmdStack):

    cmd = cmdStack[i]

    if cmd == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(-1))
    elif cmd == "size":
        print(len(arr))
    elif cmd == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif cmd[0:4] == "push":
        data = int(cmd[5:])
        arr.append(data)
    i += 1






