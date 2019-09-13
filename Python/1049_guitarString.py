a = list(map(int,input().split()))
broken = a[0]
companys = a[1]
prices = []
cost = 0
answer = 0

for i in range(companys):
    prices.append(list(map(int,input().split())))

if broken >= 6:
    for i in range(companys):
        package = prices[i][0]
        piece = prices[i][1] * 6

        if i == 0:
            if package >= piece:
                cost = piece
                continue
            elif package < piece:
                cost = package
                continue
        
        if cost >= piece or cost >= package:
            if piece > package:
                cost = package
                continue
            if piece <= package:
                cost = piece
                continue
        else:
            continue

    if cost != 0:
        answer += ( broken // 6 ) * cost
        broken = broken % 6
        cost = 0
    else:
        pass

if broken < 6:
    for i in range(companys):
        package = prices[i][0]
        piece = prices[i][1] * broken

        if i == 0:
            if package >= piece:
                cost = piece
                continue
            elif package < piece:
                cost = package
                continue
        
        if cost >= piece or cost >= package:
            if piece > package:
                cost = package
                continue
            if piece <= package:
                cost = piece
                continue
        else:
            continue
    
    answer += cost

print(answer)