n = int(input())

answers = []

for i in range(n):
    s = input()
    temp = s[::-1]
    if not temp in answers:
        if temp == s:
            print(len(s), s[len(s)//2])
            break
        else:
            answers.append(s)
    else:
        print(len(s), s[len(s)//2])
        break
