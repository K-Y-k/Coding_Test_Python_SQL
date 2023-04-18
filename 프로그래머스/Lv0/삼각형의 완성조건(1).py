def solution(sides):
    answer = 2
    
    sides.sort()
    
    if sides[2] < sides[0] + sides[1]:
        answer = 1
    
    return answer