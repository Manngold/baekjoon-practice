def solution(N, A):
    counter = [0] * N
    temp = 0
    B = set(A)
    if len(B) == 1 and list(B)[0] == N + 1:
        return counter
    for i in range(len(A)):
        if A[i] >= 1 and A[i] <= N:
            counter[A[i] - 1] += 1
            if counter[A[i] - 1] > temp:
                temp = counter[A[i] - 1]
            else:
                continue

        elif A[i] == N + 1:
            counter = [temp] * N

    return counter


# Score = 100%
# Time Complexity = O(N + M)
