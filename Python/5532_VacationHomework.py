l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

math = 0
language = 0

if b % d != 0:
    math += b // d + 1
else:
    math += b / d

if a % c != 0:
    language += a // c + 1
else:
    language += a / c

l = l - max(math, language)

if l < 0:
    print(0)
else:
    print(int(l))
