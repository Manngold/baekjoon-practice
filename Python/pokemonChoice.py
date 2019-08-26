def solution(nums):
    answer = 0
    choice = len(nums) // 2
    fixedArr = list(set(nums))
    species = len(fixedArr)
    
    if species <= choice:
        answer = species
    else:
        answer = choice
    
    return answer