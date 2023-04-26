def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in arr:
        standard = answer.pop()
        
        if i == standard:
                answer.append(i)
        else:
            answer.append(standard)
            answer.append(i)
    
    return answer