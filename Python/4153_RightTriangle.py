while True:
    triangle = sorted(list(map(int, input().split())))
    if triangle == [0, 0, 0]:
        break
    else:
        if triangle[2]**2 == triangle[1]**2 + triangle[0]**2:
            print("right")
        else:
            print("wrong")
