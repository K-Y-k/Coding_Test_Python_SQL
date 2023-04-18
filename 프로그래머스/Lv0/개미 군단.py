def solution(hp):
    answer = 0
    
    j = 5
    p = 3
    l = 1
    
    if hp // j > 0:
        answer += hp//j
        hp %= j 
    
    if hp // p > 0:
        answer += hp//p
        hp %= p 
        
    if hp // l > 0:
        answer += hp//l
        
        
    
    return answer