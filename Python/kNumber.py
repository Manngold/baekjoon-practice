def solution(array, commands):
    answer = []
    i = 0
    while i < len(commands):
        newArr = array[commands[i][0] - 1 : commands[i][1]]
        newArr.sort()
        answer.append(newArr[commands[i][2]-1])
        i += 1
    
    return answer