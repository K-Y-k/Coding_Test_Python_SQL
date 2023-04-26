def solution(n):
    answer = 0
    
    count = []
    
    
    while True:
        if n%3 == 0:
            count.append(0)
        elif n%3 != 0:
            count.append(n%3)
            
        if n//3 == 0:
            break
            
        n //= 3
    
    count.reverse()
    
    for i in range(len(count)):
        answer += count[i]* 3**(i)

    
    
    return answer