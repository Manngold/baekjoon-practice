n = int(input())

a = sorted(list(map(int, input().split())))

m = int(input())

t = list(map(int, input().split()))

for i in t:
    if i in a:
        print(1)
    else:
        print(0)
