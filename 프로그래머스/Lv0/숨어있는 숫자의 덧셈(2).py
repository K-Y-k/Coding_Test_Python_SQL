def solution(my_string):
    answer = 0
    
    standard = ""
    
    for i in my_string:
        if i.isdigit():
            standard += i
        else:
            if standard != "":
                answer += int(standard)
                standard = ""
        
    if standard != "":
        answer += int(standard)
    
    return answer