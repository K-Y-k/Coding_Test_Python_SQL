def solution(my_string):
    answer = ''
    
    a = ['a', 'e', 'i', 'o', 'u']
    
    for i in my_string:
        if i not in a:
            answer += i
    
    return answer