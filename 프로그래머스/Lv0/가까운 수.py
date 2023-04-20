def solution(array, n):
    answer = 0
    standard = n
    
    array.sort()
    
    for i in array:
        if abs(i-n) < standard:
            standard = abs(i-n)
            answer = i
    
    return answer