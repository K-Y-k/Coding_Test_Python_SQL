def solution(s):
    answer = ''
    
    for i in s:
        if s.count(i) == 1:
            answer += i
            
    s = list(answer)
    
    answer = ''.join(sorted(s))
    
    return answer