n = int(input())
answers = [0, 666]
cnt = 1666

while len(answers) <= 10000:
  if '666' in str(cnt):
    answers.append(cnt)
  cnt += 1

print(answers[n])