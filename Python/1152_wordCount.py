sentence = str(input()).upper()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = 0
idx = 0

for i in sentence:
    if i == " ":
        if idx == 0:
            idx += 1
            continue
        else:
            answer += 1
            idx += 1
            continue
        
    elif i in alphabet:
        if idx == len(sentence) - 1:
            answer += 1
            break
        else:
            idx += 1
            continue

print(answer)