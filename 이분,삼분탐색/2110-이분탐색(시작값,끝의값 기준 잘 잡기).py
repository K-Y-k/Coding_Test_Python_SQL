import sys

N, C = map(int, input().split())

C_list = []
for _ in range(N):
    Cx = int(sys.stdin.readline().rstrip())
    C_list.append(Cx)
    
C_list.sort()                                                # 오름차순으로 정렬
start = 1                                                    # 시작 값과 끝의 값의 기준을 공유기를 설치하는 거리의 기준으로 잡아야하기에 최소 간격 1과 첫집과 마지막집의 거리가 끝의 값
end = C_list[-1] - C_list[0]                                 # 최대가 될 수 있는 거리가 마지막 집 - 첫번째 집 사이 거리

while start <= end:                                          # 시작 값이 끝의 값보다 작거나 같을 때까지 반복
    mid = (start + end) // 2                                 # 중간 값 선언
    
    current_C = C_list[0]                                    # 첫번째 집에 공유기를 설치하여 초기값 지정
    count = 1                                                # 설치한 것이므로 카운트 1로 초기값
    
    for i in range(1, N):                                    # 첫번째 집은 카운트 했으므로 두번째 집부터 조회
        if C_list[i] >= current_C + mid:                     # 두번째 집이 최근 설치한 위치 + 중간 값 위치보다 크거나 같으면
            current_C = C_list[i]                            # 설치할 수 있으므로 공유기를 추가로 설치하여 최근 설치한 위치를 최신화하고   
            count += 1                                       # 공유기 설치한 횟수 증가
            
    if count >= C:                                           # 공유기 설치한 횟수가 주어진 공유기 개수보다 크거나 같으면
        start = mid + 1                                      # 우측의 데이터들을 대상으로 다시 탐색하기 위해 시작 값을 중간 값 + 1의 값으로 바꾸기
    else :                                                   # 공유기 설치한 횟수가 주어진 공유기 개수보다 작으면
        end = mid - 1                                        # 좌측의 데이터들을 대상으로 다시 탐색하기 위해 끝의 값을 중간 값 + 1의 값으로 바꾸기
        
print(end)                                                   # 위 반복문이 멈추는 순간이 시작 값이 끝의 값보다 커질 때이므로 끝의 값이 우리가 구하려는 값이다. 