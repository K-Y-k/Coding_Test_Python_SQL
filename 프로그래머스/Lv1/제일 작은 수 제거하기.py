def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
    else:
        for i in arr:
            answer.append(i)
        answer.remove(min(answer))
            
    return answer