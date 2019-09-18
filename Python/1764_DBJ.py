info = list(map(int, input().split()))

a = set()
b = set()

for i in range(info[0]):
    a.add(input())
for i in range(info[1]):
    b.add(input())

l = list(a&b)
l.sort()
print(len(l))
for i in l:
    print(i)


