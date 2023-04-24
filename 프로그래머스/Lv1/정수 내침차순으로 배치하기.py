def solution(n):
    answer = 0
    s = list(str(n))
    
    s.sort(reverse=True)
    
    answer = int("".join(s))

    return answer