def solution(box, n):
    answer = 0
    
    for i in range(len(box)):
        if i == 0:
            answer += box[i]//n
        else:
            answer *= box[i]//n
    
    return answer