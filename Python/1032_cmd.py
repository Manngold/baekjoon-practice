n = int(input())

words = []

for _ in range(n):
    words.append(list(map(str, input())))

length = len(words[0])

answer = ""

for i in range(length):
    word = words[0][i]
    for j in range(n):
        if words[j][i] == word:
            if j == n - 1:
                answer += word
            else:
                continue
        else:
            answer += "?"
            break


print(answer)
