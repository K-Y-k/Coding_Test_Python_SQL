def solution(x, n):
    answer = []
    
    count = 0
    
    for i in range(n):
        answer.append(count+x)
        count += x
    
    return answer