scale = list(map(int, input().split()))
start = 0

if scale[0] == 1:
    start = 1
    for i in scale:
        if i == start:
            start += 1
            continue
        elif i != start:
            print("mixed")
            break
    if start == 9:
        print("ascending")

else:
    start = 8
    for i in scale:
        if i == start:
            start -= 1
            continue
        elif i != start:
            print("mixed")
            break
    if start == 0:
        print("descending")
