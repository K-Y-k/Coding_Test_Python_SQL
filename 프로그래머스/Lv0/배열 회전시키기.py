def solution(numbers, direction):
    answer = []
    
    if direction == 'right':
        answer.append(numbers[len(numbers)-1])
        for i in range(len(numbers)-1):
            answer.append(numbers[i])
    else:
        for i in range(1, len(numbers)):
            answer.append(numbers[i])
        answer.append(numbers[0])
        
            
    return answer