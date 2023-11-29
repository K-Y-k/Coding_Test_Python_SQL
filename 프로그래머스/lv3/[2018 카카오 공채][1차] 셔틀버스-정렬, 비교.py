# 크루원이 도착한 시간을 정수화 처리 후 정렬하고
# 버스가 도착하는 시간 리스트를 조회하면서 버스 도착 시간내의 탑승 가능한 크루원을 최대한 넣으면서 최신화 해가고
# 최신화한 정답을 다시 시간 문자로 표현해준다.

def solution(n, t, m, timetable):
    answer = 0
    
    crew_time = []                                                      # 크루원이 도착한 시간을 정수화 처리 후 정렬
    for i in timetable:
        a, b = map(int, i.split(':'))
        crew_time.append(a*60 + b)
    crew_time.sort()
    
    busTime = [9*60 + t*i for i in range(n)]                            # 버스 시간
    
    
    i = 0                                                               # 버스에 탈 크루원의 인덱스
    for b in busTime:                                                   # 버스 도착 시간을 순회하면서
        count = 0                                                       # 현재 버스에 타는 크루원 수
        
        while count < m and crew_time[i] <= b and i < len(crew_time):   # 현재 버스 도착 시간내의 탑승 가능한 크루원을 최대한 넣고
            i += 1
            count += 1
            
        if count < m:                                                   # 현재 버스에 자리가 남았으면 현재 버스 도착 시간에 내가 타는 것으로 최신화
            answer = b
        else:                                                           # 현재 버스에 자리가 없으면 제일 마지막 크루원의 도착 시간보다 1분전에 도착하는 것으로 최신화
            answer = crew_time[i-1] - 1
    
    
    # 정답을 다시 시간 문자로 표현
    h = answer // 60
    m = answer % 60
    
    if h < 10:
        h = '0' + str(h)
    
    if m < 10:
        m = '0' + str(m)
    
    answer_ = str(h) + ':' + str(m)
    

    return answer_