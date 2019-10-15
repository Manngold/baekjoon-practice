info = []
cnt = 0
for _ in range(3):
    info.append(list(map(int,input().split())))

for i in range(3):
    for j in range(4):
        if info[i][j] == 0:
            cnt += 1
        else:
            continue
    if cnt == 1:
        print("A")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("C")
    elif cnt == 4:
        print("D")
    else:
        print("E")
    cnt = 0
