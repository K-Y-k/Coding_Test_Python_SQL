def solution(my_str, n):
    answer = []
    
    temp = ''
    
    for i in range(len(my_str)):
        temp += my_str[i]
        
        if (i+1) % n == 0:
            answer.append(temp)
            temp = ''
        
    if len(temp) > 0:
        answer.append(temp)
        temp = ''
    
    return answer