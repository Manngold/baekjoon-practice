string = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = []

for i in alphabet:
    idx = 0
    if i in string:
        for j in string:
            if i != j:
                idx += 1
                continue
            if i == j:
                answer.append(idx)
                break

    else:
        answer.append(-1)

print(" ".join(map(str, answer)))
