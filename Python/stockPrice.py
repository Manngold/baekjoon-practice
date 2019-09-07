def solution(prices):
    answer = []
    i = 0
    j = i + 1
    count = 0
    while i < len(prices):
        if i == len(prices) - 1:
            answer.append(count)
            break
        else:
            while j < len(prices):
                if prices[i] <= prices[j]:
                    count += 1
            j += 1

        answer.append(count)
        i += 1
        count = 0



    return answer