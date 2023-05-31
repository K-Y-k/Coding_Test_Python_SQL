# 잃어버린 학생과 여분이 있는 학생이 둘 다인 경우가 있을 수 있다.
# 즉, set()으로 묶어서 서로 빼주어 겹치지 않게 진행을 해줘야한다.

# 또한 그 이후 나는 각 케이스에 따른 조건을 생각하고 선언하였다.



def solution(n, lost, reserve):
    answer = 0

    new_lost = set(lost) - set(reserve)                             # 서로 안 겹친 잃어버린 학생
    new_reserve = set(reserve) - set(lost)                          # 서로 안 겹친 여분이 있는 학생 
    
    for i in new_lost:                                              # 읽어버린 학생을 조회해서 각 위치의 학생의 여분에 따른 조건 적용
        if i-1 in new_reserve and i+1 not in new_reserve:           # 앞 학생만 여분이 있는 경우
            new_reserve.remove(i-1)
        elif i+1 in new_reserve and i-1 not in new_reserve:         # 뒤 학생만 여분이 있는 경우 
            new_reserve.remove(i+1)                                 
        elif i-1 in new_reserve and i+1 in new_reserve:             # 앞, 뒤 학생 모두 여분이 있는 경우 
            new_reserve.remove(i-1)
        elif i+1 not in new_reserve and i-1 not in new_reserve:     # 앞, 뒤 학생 모두 여분이 없는 경우 
            n -= 1                                                  # 체육 수업을 참여 못하는 것이 확정이므로 전체 학생에 -1
            
    answer = n                                         
    return answer