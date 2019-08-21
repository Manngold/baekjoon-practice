def solution(L, x):
    answer = []
    listLength = len(L)-1
    i = 0
    while i <= listLength:
        if(L[i] == x):
            answer.append(i)
            i += 1
        else:
            i += 1
    if len(answer) == 0:
        answer.append(-1)
    return answer