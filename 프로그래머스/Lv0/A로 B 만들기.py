def solution(before, after):
    answer = 0
    count = 0
    
    for i in before:
        if i in after:
            if before.count(i) == after.count(i):
                count += 1
    
    if count == len(before):
        answer = 1
    else: 
        answer = 0
    
    return answer