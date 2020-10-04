n = int(input())

step = [1]
cnt = 1

while step[-1] < n:
  step.append(step[-1] + cnt * 6)
  cnt += 1

print(len(step))
