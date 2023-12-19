# 내가 푼 방식 - 시간 초과
# 무적권의 개수 만큼 반복하여 적 큐의 제일 높은 값을 지운 후 앞에 0으로 넣고
# 적 큐를 조회하며 준호의 병사를 차감한 후 준호 병사가 남아있으면 정답에 카운팅하고
# 준호의 병사가 0보다 작아지면 벗어나게 했다.

# 하지만 이렇게 하면 문제에서 주어진 범위가 너무 넓어 시간 초과 발생
# 1 ≤ n ≤ 1,000,000,000
# 1 ≤ k ≤ 500,000
# 1 ≤ enemy의 길이 ≤ 1,000,000

from collections import deque

def solution(n, k, enemy):
    answer = 0
    
    enemy = deque(enemy)
    
    for _ in range(k):
        enemy.remove(max(enemy))
        enemy.appendleft(0)
    
    for i in range(len(enemy)):
        n -= enemy[i]
        
        if n < 0:
            break
        else:
            answer += 1
    
    
    return answer



# 힙을 활용하여
# 적 리스트의 값을 힙에 넣고
# 힙의 길이가 무적권의 개수보다 클 때부터 넣었던 힙의 제일 앞의 값을 빼서 준호의 병사에 차감해간다.
# 그 후 만약 준호의 병사가 0보다 작어지면 현재 인덱스가 최대 라운드이므로 현재 인덱스로 반환한다.

# 만약 준호의 병사가 더 많아서 적 리스트를 모두 사용했을 수도 있으므로 for 문을 벗어날 경우는 이 경우이므로
# 적 리스트의 길이가 최대 라운드이므로 이를 반환한다.

import heapq

def solution(n, k, enemy):
    heap = []
    
    for i, j in enumerate(enemy):
        heapq.heappush(heap, j)          # 적 리스트의 값을 힙에 넣고
        
        
        if len(heap) > k:               # 힙의 길이가 무적권의 개수보다 클 때부터
            n -= heapq.heappop(heap)    # 넣었던 힙의 제일 앞의 값을 빼서 준호의 병사에 차감해간다.
        
        if n < 0:                       # 그 후 만약 준호의 병사가 0보다 작어지면
            return i                    # 현재 인덱스가 최대 라운드이므로 현재 인덱스로 반환한다.


    return len(enemy)                   # 만약 준호의 병사가 더 많아서 적 리스트를 모두 사용했을 수도 있으므로 for 문을 벗어날 경우는 이 경우이므로
                                        # 적 리스트의 길이가 최대 라운드이므로 이를 반환한다.