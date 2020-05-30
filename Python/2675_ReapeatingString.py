n = int(input())

for i in range(n):
    repeat, s = map(str, input().split())
    answer = ""
    for j in s:
        answer += j * int(repeat)
    print(answer)
