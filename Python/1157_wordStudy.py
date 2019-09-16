word = str(input())
word = word.upper()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

status = {}
answer = []

for i in word:
    if i in alphabet:
        if i in status:
            status[i] += 1
            continue
        elif not i in status:
            status[i] = 1
            continue

for i in status:
    if len(answer) == 0:
        answer.append(i)
        continue
    elif status[answer[-1]] < status[i]:
        while len(answer) != 0:
            answer.pop()
        answer.append(i)
        continue
    elif status[answer[-1]] == status[i]:
        answer.append(i)
        continue
    elif status[answer[-1]] > status[i]:
        continue

if len(answer) > 1:
    print("?")
elif len(answer) == 1:
    print(answer[-1])




