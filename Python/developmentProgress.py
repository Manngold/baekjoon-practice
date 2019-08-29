def solution(progresses, speeds):
    answer = []
    i = 0
    complete = 0

    while len(progresses) != 0:
        progresses[i] += speeds[i]
        if progresses[i] >= 100:
            if i == 0:
                del progresses[i]
                del speeds[i]
                complete += 1
                continue
        
        if i == len(progresses) - 1:
            if complete != 0:
                answer.append(complete)
            complete = 0
            i = 0
            continue
        
        i += 1
    answer.append(complete)

    return answer