def solution(my_string, num1, num2):
    answer = ''
    
    a = list(my_string)
    
    a[num1], a[num2] = a[num2], a[num1]
    
    answer = ''.join(a)
    
    
    return answer