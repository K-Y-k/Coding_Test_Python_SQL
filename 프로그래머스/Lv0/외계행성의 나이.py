def solution(age):
    answer = ''
    
    a = list(map(int, str(age)))
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    for i in a:
        answer += alphabet[i]
        
    return answer