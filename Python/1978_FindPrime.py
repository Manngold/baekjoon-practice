n = int(input())

arr = list(map(int, input().split()))
answer = 0


def isPrime(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


for i in arr:
    if isPrime(i):
        answer += 1

print(answer)
