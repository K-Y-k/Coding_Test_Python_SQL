def solution(seoul):
    answer = ''
    
    count = 0
    
    for i in seoul:
        if i == 'Kim':
            answer = '김서방은 ' + str(count) + '에 있다'
            
        count += 1
        
    return answer