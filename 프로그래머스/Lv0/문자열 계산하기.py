def solution(my_string):
    answer = 0
    
    my_string_split = list(map(str, my_string.split(' ')))
    
    op = ''
    
    for i in my_string_split:
        if i == '+':
            op ='+'
        elif i == '-':
            op = '-'  
        elif i.isdigit() and op == '':
            answer += int(i)
        elif i.isdigit() and op == '+':
            answer += int(i)
            op = ''
        elif i.isdigit() and op == '-':
            answer -= int(i)
            op = ''
    
    return answer