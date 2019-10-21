n = int(input())

no = 0
yes = 0

for _ in range(n):
    answer = int(input())
    if answer == 1:
        yes += 1
    elif answer == 0:
        no += 1
    
if yes > no:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")