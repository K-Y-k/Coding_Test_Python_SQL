# [진입, 진출]의 리스트로 구성된 경로 리스트를 진출 기준 오름차순으로 정렬한 후,
# 기준 값을 문제에서 주어진 올 수 있는 최솟값이 -30000보다 작은 -30001로 잡고
# 경로 리스트를 하나씩 조회해가며
# 현재 경로의 진입 값이 기준 값보다 크다면
# 새로운 카메라를 설치해야 한다는 뜻이므로 기준 값을 현재 경로의 진출 값으로 변경하고 카메라 설치 개수에 +1한다.

def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[1])     # [진입, 진출]의 리스트로 구성된 경로 리스트를 진출 기준 오름차순으로 정렬한 후,
    
    standard_route = -30001            # 기준 값을 문제에서 주어진 올 수 있는 최솟값이 -30000보다 작은 -30001로 잡고
     
    
    for i in routes:                   # 경로 리스트를 하나씩 조회해가며
        if i[0] > standard_route:      # 현재 경로의 진입 값이 기준 값보다 크다면
            standard_route = i[1]      # 새로운 카메라를 설치해야 한다는 뜻이므로 기준 값을 현재 경로의 진출 값으로 변경하고
            answer += 1                # 카메라 설치 개수에 +1한다.
    
    return answer