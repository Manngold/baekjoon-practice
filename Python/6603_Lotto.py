from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    if n == 0:
        break
    else:
        answer = list(combinations(arr, 6))
        for i in answer:
            i = str(i).replace("(", "")
            i = str(i).replace(")", "")
            i = str(i).replace(",", "")
            print(i)
        print("")
