def solution(num, k):
    answer = -1
    
    num_list = list(map(int, str(num)))
    
    if num_list.count(k) == 0:
        return answer
    else:
        for i in range(len(num_list)):
            if num_list[i] == k:
                answer = i+1
                break
    
    return answer