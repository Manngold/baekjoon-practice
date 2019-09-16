students = list(map(int, input().split()))

girl = students[0]
boy = students[1]
intern = students[2]
answer = 0

while intern != 0:
    if girl / 2 > boy:
        girl -= 1
        intern -= 1
        continue
    elif girl / 2 == boy:
        if intern >= 2:
            girl -= 1
            boy -= 1
            intern -= 2
            continue
        if intern < 2:
            girl -= 1
            intern -= 1
            continue
    elif girl / 2 < boy:
        boy -= 1
        intern -= 1
        continue

if girl // 2 >= boy:
    answer = boy
elif girl // 2 < boy:
    answer = girl // 2

print(answer)
    

