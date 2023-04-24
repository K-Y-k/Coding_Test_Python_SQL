def solution(phone_number):
    answer = ''
    
    a = list(phone_number)
    n = len(phone_number)
    
    if n > 4:
        for i in range(0, n-4):
            answer += '*'
        for i in range(n-4, n):
            answer += a[i]  
    else:
        answer = phone_number
        
    return answer