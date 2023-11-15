# 받아온 손님이 오는 시간을 리스트로 담고 해당 리스트를 작은 순으로 정렬한다.
# M, 2M, 3M, ... 초 마다 K, 2K, 3K의 붕어빵이 남는다.
# 그렇다면 x초 일때의 붕어 생산량에서 그 전에 사간 사람의 수를 빼면 x초의 붕어빵 재고를 알 수 있다.
# 이 재고가 음수이면 해당 초에 온 손님은 못사므로 불가능으로 설정한다.

T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    
    visit_time = list(map(int, input().split()))    # 받아온 손님이 오는 시간을 리스트로 담고
    visit_time.sort()                               # 해당 리스트를 작은 순으로 정렬한다.
    
    answer = 'Possible'
    
    for idx, value in enumerate(visit_time):
        possible = (value // M) * K - (idx+1)       # x초 일때의 붕어 생산량에서 그 전에 사간 사람의 수를 빼면 x초의 붕어빵 재고를 알 수 있다.
        
        if possible < 0:                            # 이 재고가 음수이면
            answer = "Impossible"                   # 현재 초에 온 손님은 못사므로 불가능으로 설정한다.
            break
            
    print('#' + str(test_case), answer)
    