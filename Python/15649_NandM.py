from itertools import permutations

n, m = map(int, input().split())

nums = []

for i in range(1, n + 1):
    nums.append(str(i))

answers = list(permutations(nums, m))

for i in answers:
    print(" ".join(list(i)))
