
def solution(A):
    arr = sorted(list(set(A)))
    temp = 0
    if arr[-1] < 0:
        return 1
    for i in range(len(arr)):
        if arr[i] <= 0:
            continue
        else:
            if arr[i] == temp:
                temp += 1
            else:
                return temp
    return temp

# Score = 100
# Time Complexity = O(N) or O(Nlog(N))
