import math

start, end = map(int, input().split())
answer = []


def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)+1)):
        if(a % i == 0):
            return False
    answer.append(a)


for i in range(start, end + 1):
    isPrime(i)

for i in answer:
    print(i)
