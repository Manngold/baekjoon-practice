
def solution(X, A):
    checkArr = set([])
    for i in range(len(A)):

        if A[i] <= X:
            checkArr.add(A[i])
            if len(checkArr) == X:
                return i
            else:
                continue
        else:
            continue
    return - 1

# Score = 100%
# Time Complexity = O(N)
