n = str(input())
cnt = 0

if len(n) == 1:
    n = "0"+n

target = n

while True:
    if len(n) == 1:
        n = "0" + n
    result = str(int(n[0]) + int(n[1]))
    if len(result) == 1:
        result = "0"+result
    cnt += 1
    if n[1] + result[1] == target:
        print(cnt)
        break
    else:
        n = n[1] + result[1]

