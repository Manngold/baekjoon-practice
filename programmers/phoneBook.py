def solution(phone_book):
  for i in range(len(phone_book)):
      l = len(phone_book[i])
      for j in range(len(phone_book)):
          if len(phone_book[j]) < l or j == i:
              continue
          elif phone_book[i] == phone_book[j][0:l]:
              answer = False
              return answer
  answer = True
  return answer