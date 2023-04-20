def solution(spell, dic):
    answer = 2
    count = 0
    
    for i in dic:
        for j in spell:
            if j in i:
                count += 1
                
            if count == len(spell):
                answer = 1
        count = 0
            
    return answer