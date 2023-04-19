def solution(rsp):
    answer = ''
    
    rock = '0'
    sissor = '2'
    papper = '5'
    
    
    for i in rsp:
        if i == rock:
            answer += papper
        elif i == sissor:
            answer += rock
        else:
            answer += sissor
            
    
    return answer