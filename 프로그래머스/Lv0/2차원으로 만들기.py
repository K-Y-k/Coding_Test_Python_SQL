def solution(num_list, n):
    answer = []
    standard = []
        
    for i in range(len(num_list)):
        standard.append(num_list[i])
        
        if (i+1) % n == 0 :
            answer.append(standard)
            standard = []
    
    return answer