def solution(n):
  answer = ''
  watermelon = "수박"
  answer += watermelon * (n // 2)
  if n % 2:
    answer += "수"
  return answer