from collections import deque

n, k = map(int, input().split())

arr = deque(map(int, input().split()))

socket = []
answer = 0

while arr:
    device = arr.popleft()
    if device in socket:
        continue
    if len(socket) < n:
        socket.append(device)
    else:
        for i in range(n):
            if not socket[i] in arr:
                socket[i] = device
                answer += 1
                break
            if i == n - 1 and socket[i] in arr:
                checker = [0] * n
                for j in range(n):
                    for k in range(len(arr)):
                        if socket[j] == arr[k]:
                            checker[j] = k
                            break
                socket[checker.index(max(checker))] = device
                answer += 1


print(answer)
