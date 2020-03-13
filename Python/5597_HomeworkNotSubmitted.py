students = [0 for i in range(31)]

for _ in range(28):
    num = int(input())
    students[num] = 1

for i in range(1, len(students)):
    if students[i] == 0:
        print(i)
