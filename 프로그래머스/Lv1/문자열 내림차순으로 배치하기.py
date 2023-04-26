def solution(s):
    answer = list((s))
    
    answer.sort(reverse=True)
    
    answer = str("".join(answer))

    
    return answer