def solution(n):
    answer = 0
    
    count = 1
    pizza_slice = 6
    
    while True:
        if pizza_slice*count % n == 0:
            answer = count
            break
        count += 1
    
    
    return answer