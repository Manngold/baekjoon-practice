roomNumber = str(input())

numbers = {
    '0' : 0,
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
    '7' : 0,
    '8' : 0,
    '9' : 0
    }

answer = 0

def addNumbers():
    for i in numbers:
        numbers[i] += 1

for i in roomNumber:
    if numbers[i] == 0:
        if i == "6":
            if numbers['9'] != 0:
                numbers['9'] -= 1
                continue
            elif numbers['9'] == 0:
                addNumbers()
                answer += 1
                numbers[i] -= 1
                continue
        elif i == "9":
            if numbers['6'] != 0:
                numbers['6'] -= 1
                continue
            elif numbers['6'] == 0:
                addNumbers()
                answer += 1
                numbers[i] -= 1
                continue
        else:
            answer += 1
            addNumbers()
            numbers[i] -= 1
            continue
    elif numbers[i] != 0:
        numbers[i] -= 1
        continue

print(answer)




