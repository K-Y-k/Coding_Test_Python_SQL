def solution(price, money, count):
    answer = 0
    total = 0
    
    for i in range(1, count+1):
        total += price * i
        
    if money - total < 0 :
        answer = abs(money - total)
    else:
        return 0

    return answer