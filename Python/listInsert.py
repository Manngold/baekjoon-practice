def solution(L, x):
    listLength = len(L)-1
    i = 0
    while i <= listLength:
        if(x < L[i]):
            L.insert(i, x)
            break
        elif(x > L[listLength]):
            L.append(x)
            break
        else:
            i += 1
    answer = L
    return answer