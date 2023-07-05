# 내가 푼 방식
# sides에 있는 선분이 가장 긴 경우와
# sides에 없는 새로운 선분이 가장 긴 경우를 각 구해주었다.


def solution(sides):
    answer = 0
    
    sides_max = max(sides)
    sides_min = min(sides)
    
    # sides에 있는 선분이 가장 긴 경우
    new_sides = sides_max - sides_min + 1   # sides에 있는 선분이 가장 긴 경우일 때의 새로운 선분을 최소의 값부터 적용
    sides_max_count = 0                     # 카운팅할 변수 초기화 및 선언
    
    for i in range(new_sides, sides_max+1): # 최소 값부터 최대 값까지 카운팅
        sides_max_count += 1
        
    answer += sides_max_count               # 정답에 적용
    
    
    # sides에 없는 새로운 선분이 가장 긴 경우
    new_sides_max = sides_max+1                      # 새로운 선분이 가장 긴 경우의 새로운 선분을 최소의 값부터 적용
    
    if new_sides_max < sides_max+ sides_min:         # 새로운 선분이 가장 긴 경우가 가능한 sides인 경우
        new_sides_max_count = 0                      # 카운팅할 변수 초기화 및 선언
        
        while new_sides_max < sides_max + sides_min: # 삼각형의 조건이 안될 때까지 반복하여 카운팅
            new_sides_max_count += 1
            new_sides_max += 1
            
        answer += new_sides_max_count                # 정답에 적용
    
    
    return answer