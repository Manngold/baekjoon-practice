n = input()

answer = 0

alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

pre = ["c", "d", "l", "n", "s", "z"]

temp = ""

for i in alphabet:
    if i in n:
        n = n.replace(i, "*")

answer = len(n)

print(answer)
