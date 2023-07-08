# 내가 푼 방식 : 테스트케이스 하나만 맞춤..
# 다리를 건너는 트럭과 대기중인 트럭이 모두 없어질 때까지 옮기는 작업을 했지만 문제의 의도를 잘못 파악함

def solution(bridge_length, weight, truck_weights):
    time = 0
    crossing_truck = []
    
    while True:
        if len(truck_weights) == 0 and len(crossing_truck) == 0:
            break
            
        if truck_weights:
            if sum(crossing_truck) + truck_weights[0] <= weight and len(crossing_truck) < bridge_length:
                temp = truck_weights.pop(0)
                crossing_truck.append(temp) 
                time += 1
            else:
                crossing_truck.pop(0)
                time += 1 
        else:
            crossing_truck.pop(0)
            time += 1     
    
    return time



# 문제에서는 다리 길이 만큼의 트럭이 이동되는 것이었다.
# 예시를 다리 길이가 2이고 7,4,5,6의 트럭이 있다고하면

# 현재까지 걸린 시간     다리에 있는 트럭       대기중인 트럭 
#       1초                0, 7                 4,5,6
#       2초                7, 0                 4,5,6
#       3초                0, 4                 5,6

# 이처럼 주어진 다리 길이만큼의 이동이 또 1초가 걸리는 것이었다. 
# 즉 다리에 있는 트럭 리스트를 다리 길이만큼 생성하고 이동하는 연산까지 추가해야했다.

# 여기서 시간 효율을 더 올리기
# 1) 일반 리스트의 pop(0)은 시간복잡도가 O(n)이지만 
#    deque의 popleft()는 시간복자도가 O(1)로 훨씬 빠르다.
# 2) sum()함수 보다 하나의 변수에 축적하는 방식이 훨씬 빠르다.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)              # 더 빠르게 하기 위해 deque로 선언
    bridge = deque([0] * bridge_length)               # 다리 길이만큼 이동하는 연산까지 해야하기에 다리 길이만큼 초기화
    bridge_sum = 0                                    # sum함수 대신 축적하기위해 선언 
    
    while len(bridge):
        time += 1
        crossing_complete_truck = bridge.popleft()       # 현재 다리에 있는 트럭을 도착지점으로 옮기기 위해 꺼내오고
        bridge_sum -= crossing_complete_truck            # 도착지점에 옮겼으므로 현재 다리의 최종 트럭 무게를 최신화하고
        
        if truck_weights:                                # 아직 대기중인 트럭이 있으면
            if bridge_sum + truck_weights[0] <= weight:  # 대기중인 트럭이 들어오면 최대 무게까지 가능하다면    
                temp = truck_weights.popleft()           # 대기중인 트럭을 꺼내와서
                bridge.append(temp)                      # 다리에 있는 트럭 리스트에 넣고
                bridge_sum += temp                       # 현재 다리의 최종 트럭 무게를 최신화한다.

            else:                                        # 최대 무게까지 불가능하다면
                bridge.append(0)                         # 0을 넣는다.
    
    return time