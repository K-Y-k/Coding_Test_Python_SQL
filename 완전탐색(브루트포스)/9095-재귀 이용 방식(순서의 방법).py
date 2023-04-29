# 문제에서 개수가 11미만인 양수까지만 올수 있으므로 최대 10가지를 선택할 수 있다.
# 즉, 방법의수는 1,2,3을 10가지로 3^10으로 이 값은 1억가지(=1초)보다 작아 충분히 빠르게 돌아가므로
# 모두 조회하는 브루트 포스의 재귀 방식으로 접근할 수도 있다는 것이다.

# 재귀로 구현하므로 각 케이스에 맞게 구현해야한다.
# Case1. 정답보다 초과하여 불가능한 경우                   : sum > goal
# Case2. 정답을 찾은 경우                                 : sum = goal
# Case3. 아직 정답을 못찾아서 다음 경우를 재귀 호출하는 경우 : go(sum+i, goal)


import sys

def go(sum_total, goal):
    if sum_total > goal:                     # Case1. 정답보다 초과하여 불가능한 경우 0으로 반환하여 총 개수에 영향을 주지 않는다.
        return 0
    elif sum_total == goal:                  # Case2. 정답을 찾은 경우 정답이 올 수 있는 총 개수를 출력하는 것이 문제이므로 1가지를 찾은 것이니 1로 반환
        return 1
    else:                                    # Case3. 아직 정답을 못찾아서 다음 경우를 재귀 호출하는 경우
        count = 0                              
        
        for i in range(1, 4):                # 문제에서 원하는 1,2,3에 따른 총 방법의 수 구하기 위한 모두 조회의 반복 
            count += go(sum_total+i, goal)   # 재귀를 호출하여 위 Case2인 경우들의 개수 합으로 구해질 것이다.
            
        return count
    
    
T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(go(0, n))                          # 재귀를 호출하여 최종 count가 나오는 것이 출력됨