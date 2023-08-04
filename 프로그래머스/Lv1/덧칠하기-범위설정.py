# 한번 페인트 칠할 떄의 범위가 m이므로
# 칠해야 하는 페인트의 section이 오름차순으로 되어있으므로
# 제일 앞의 값에서 페인트 한번 칠할 때의 최대 거리로 기준을 잡아서
# 제일 앞의 값부터 차례로 최대 거리까지의 section은 모두 제거해준 후 덧칠한 카운팅을 해주면 된다.


def solution(n, m, section):
    answer = 0
    
    while section:
        paint_section = section[0] + m                   # 제일 앞의 값에서 페인트 한번 칠할 때의 최대 거리로 기준을 잡아서
        
        while section and section[0] < paint_section:    # 제일 앞의 값부터 차례로 최대 거리까지의 section은
            section.pop(0)                               # 모두 제거해준 후 
            
        answer += 1                                      # 덧칠한 카운팅을 해주면 된다.
                
                
    return answer