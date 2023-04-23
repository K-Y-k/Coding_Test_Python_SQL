def solution(n):
    count = 1
    
    while True:
        if n % count == 1:
            break
        count += 1
    
    answer = count 
    return answer