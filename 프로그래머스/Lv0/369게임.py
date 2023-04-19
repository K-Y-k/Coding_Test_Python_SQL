def solution(order):
    answer = 0
    
    order_list = list(map(int, str(order)))
    
    for i in order_list:
        if i != 0 and i % 3 == 0:
            answer += 1
    
    return answer