def solution(s):
    answer = 0
    
    s_list_split = list(map(str, s.split(' ')))
    s_list = []
    
    for i in s_list_split:
        if i.isdigit():
            s_list.append(int(i))
                
        elif i == 'Z':
            if len(s_list) != 0:
                s_list.pop()
                
        else:
            s_list.append(int(i))
                
                
    answer = sum(s_list)
    
    return answer