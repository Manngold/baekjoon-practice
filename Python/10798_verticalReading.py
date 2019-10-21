board = []
length = []
answer = ""
idx = 0

for i in range(5):
    board.append(str(input()))
    length.append(len(board[i]))

for i in range(max(length)):
    for j in range(5):
        if idx >= len(board[j]):
            continue
        else:
            answer += board[j][i]
    idx += 1
        

print(answer)