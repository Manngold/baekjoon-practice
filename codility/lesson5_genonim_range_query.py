DNA = {
    'A': 1,
    'C': 2,
    'G': 3,
    'T': 4
}


def solution(S, P, Q):
    answer = []
    for i in range(len(P)):
        arr = []
        for k in range(P[i], Q[i] + 1):
            arr.append(DNA[S[k]])
        sortedArr = sorted(arr)

        answer.append(sortedArr[0])

    return answer
