def solution(s):
    answer = ''
    
    length = len(s)//2
    
    if len(s) % 2 == 1:
        answer = s[length]
    else:
        answer = s[length-1] + s[length]
    
    
    return answer