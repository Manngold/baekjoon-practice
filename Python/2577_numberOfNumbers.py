a = int(input())
b = int(input())
c = int(input())

nums = {
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0,
}

target = a * b * c

parsedTarget = str(target)

for i in parsedTarget:
    nums[i] += 1

for i in range(10):
    print(nums[str(i)])