n, k = map(int, input().split())

arr = []
multi = 2


for i in range(2, n + 1):
    if not i in arr:
        arr.append(i)
        if len(arr) == k:
            print(arr[-1])
            break
    while multi * i <= n:
        if not multi * i in arr:
            arr.append(multi * i)
            if len(arr) == k:
                print(arr[-1])
                break
            multi += 1
        else:
            multi += 1
    multi = 2



        

    

        

    




