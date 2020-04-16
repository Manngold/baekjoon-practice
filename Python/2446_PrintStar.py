n = int(input())

star = "*"
blank = " "
if n > 1:
    for i in range(n):
        answer = ""
        answer += blank * i
        answer += star * ((n * 2 - 1) - (i * 2))
        print(answer)

    for i in range(n-2, -1, -1):
        answer = ""
        answer += blank * i
        answer += star * ((n * 2 - 1) - (i * 2))
        print(answer)
else:
    print("*")
