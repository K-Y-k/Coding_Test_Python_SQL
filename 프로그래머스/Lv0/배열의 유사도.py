def solution(s1, s2):
    answer = 0
    
    for i in s1:
        for j in s2:
            if j == i:
                answer += 1
    
    return answer