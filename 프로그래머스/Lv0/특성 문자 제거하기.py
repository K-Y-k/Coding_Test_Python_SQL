def solution(my_string, letter):
    answer = ''
    
    for i in my_string:
        if i == letter:
            continue
        answer += i
    
    
    return answer