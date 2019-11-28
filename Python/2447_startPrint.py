n = int(input())
cnt = 0

answer = [["*"]*n]*n

while n != 1:
    n = n / 3
    cnt += 1
