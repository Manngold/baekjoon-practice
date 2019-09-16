num = input()
answer = ""

l = []

for i in num:
    l.append(int(i))


if not "0" in num or sum(l) % 3 != 0:
    answer = -1

else:
    l.sort(reverse=True)
    for i in range(len(l)):
        answer += str(l[i])
    
print(answer)

    