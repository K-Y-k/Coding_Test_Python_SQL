def solution(num_list):
    answer = []
    
    even = []
    odd = []
    
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
            
    answer.append(len(even))
    answer.append(len(odd))

    return answer