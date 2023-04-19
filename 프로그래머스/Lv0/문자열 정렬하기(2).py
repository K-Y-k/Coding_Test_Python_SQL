def solution(my_string):
    answer = []
    
    for i in my_string:
        if i == i.upper():
            answer.append(i.lower())
        else:
            answer.append(i)
            
    answer.sort()
    
    answer = ''.join(answer)

    
    return answer