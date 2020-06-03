n = int(input())

answer = 0
isValid = True

while isValid:
    for i in range(n, 0, -1):
        s = str(i)
        temp = 0
        for j in s:
            temp += int(j)
        temp += i

        if temp == n:
            answer = i
            isValid = False
        if temp < n or i == 1:
            isValid = False

print(answer)
