def solution(L, x):
    lower = 0
    upper = len(L)-1
    answer = -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            answer = middle
            break
        elif L[middle] < x:
            lower = middle + 1
            continue
        elif L[middle] > x:
            upper = middle - 1
            continue
    return answer