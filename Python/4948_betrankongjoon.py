import math
case = []
primes = []
while True:
    a = int(input())
    if a != 0:
        case.append(a)
    else:
        break

def isPrime(num):
    for i in range(2, round(num ** 0.5 + 1)):
        if num % i == 0:
            return 0
    primes.append(num)

for i in case:
    for j in range(i + 1, (i * 2) + 1):
        isPrime(j)
    print(len(primes))
    primes = []
    




