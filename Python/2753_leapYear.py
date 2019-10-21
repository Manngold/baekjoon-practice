year = str(input())

if year[-1] == "0" and year[-2] == "0":
    if int(year) % 400 == 0:
        print("1")
    else:
        print("0")
else:
    if int(year) % 4 == 0:
        print("1")
    else:
        print("0")