# 징검다리를 k만큼 건너뛸 수 없을 때만큼 하나씩 조회해가며 구현했지만
# 테케 실패 및 시간초과

def solution(stones, k):
    answer = 0
    bool_ = True
    
    while bool_:
        for i, value in enumerate(stones):
            if value > 0:
                stones[i] -= 1
            else:
                if i == len(stones)-1 or i < len(stones)-k-1 and sum(stones[i:i+k]) > 0:
                    continue
                else: 
                    bool_ = False
                    break
                
        answer += 1
                    
    return answer



# 효율성까지 활용한 이분탐색 방법
# 디딤돌을 건너는 기준이 아닌 디딤돌 숫자에 중점을 둔 방식으로
# 시작과 끝은 디딤돌의 최소 숫자와 최대 숫자를 기준으로 초기화하고

# 중간 값을 선언한 값을 빼가며 0이하일 경우 현재 디딤돌을 못건너는 곳이므로 건너 뛰어야하는 카운트를 카운팅해주면서
#                            0보다 크면   현재 돌을 건넜다는 뜻이므로 연속으로 건너는 뛰어야하는 카운팅을 다시 초기화

# 연속된 카운팅이 k개보다 크거나 같게 되면 멈추고
# 카운팅한 값이 k개보다 크거나 같으면 끝의 값을 중간값 - 1로 갱신해주고
#              k개보다 작으면        현재 start~end구간에서는 끝까지 건널 수 있다는 뜻이므로 시작의 값을 중간값 + 1로 갱신해준다.

def solution(stones, k):
    start = 1              # 최소 숫자(문제에서 최소 1이라고 주어짐)와
    end = max(stones)      # 최대 숫자를 기준으로 선언
    
    while start <= end:
        mid = (start + end) // 2    # 현재 건너는 사람 수를 선언
        count = 0                   # 건너뛰어야하는 카운트 선언
        
        for stone in stones:        # 중간 값을 선언한 값을 빼가며
            if stone - mid <= 0:    # 0이하일 경우 현재 디딤돌을 못건너는 곳이므로
                count += 1          # 건너 뛰어야하는 카운트를 카운팅해주면서
            else:                   # 0보다 크면 현재 돌을 건넜다는 뜻이므로
                count = 0           # 연속으로 건너는 뛰어야하는 카운팅을 다시 초기화
                
            if count >= k:          # 카운팅한 값이 k개 이상이 되면
                break               # 더이상 건널 수 없으므로 루프 종료
                
        if count >= k:              # 카운팅한 값이 k개보다 크거나 같으면
            end = mid - 1           # 끝의 값을 중간값 - 1로 갱신해주고
        else:                       # k개보다 작으면 현재 start~end구간에서는 끝까지 건널 수 있다는 뜻이므로
            start = mid + 1         # 시작의 값을 중간값 + 1로 갱신해준다.
        

    return start