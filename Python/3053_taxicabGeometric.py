import math

r = float(input())

euclid = round(r ** 2 *math.pi, 6)
taxicab = round(r ** 2 * 2, 6)

print(euclid)
print(taxicab)