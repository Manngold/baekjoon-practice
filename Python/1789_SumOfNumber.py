s = int(input())

ans = 0
n = 0
i = 1

while n < s:
    n = n + i
    ans += 1
    if s - n > i:
        i += 1
        continue
    elif s - n < i:
        while s - n >= i:
            i -= 1
            n = n - i
            ans -= 1
        break
    else:
        break


print(ans)
