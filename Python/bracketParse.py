def solution(s):
    answer = True
    left = 0
    right = 0
    idx = 0
    while idx < len(s):
        if s[0] == ")":
            answer = False
            break
        else:
            if s[idx] == "(":
                left += 1
                idx += 1
                continue
            else:
                right += 1
                if left < right:
                    answer = False
                    break
                else:
                    idx += 1
                    continue
    if left != right:
        answer = False
    return answer