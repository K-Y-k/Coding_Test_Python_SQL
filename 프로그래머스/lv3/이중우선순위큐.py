# 연산 명령과 숫자를 나누고 각 케이스에 맞는 명령에 따라
# 숫자 삽입할 때는 heappush())를 사용하고
# 최솟값 삭제할 때는 heappop()을 사용하고
# 최댓값을 삭제할 때는 max()를 사용한다.

import heapq                                        # 힙 모듈 사용

def solution(operations):
    answer = []
    queue = []
    
    for i in operations:
        operation, num = i.split(' ')               # 연산 명령과 숫자를 나누고
        
        if operation == 'I':                        # 각 케이스에 맞는 명령에 따라
            heapq.heappush(queue, int(num))         # 숫자 삽입할 때는 heappush())를 사용하고
        elif operation == 'D' and num == '-1':
            if len(queue) != 0:
                heapq.heappop(queue)                # 최솟값 삭제할 때는 heappop()을 사용하고
        else:
            if len(queue) != 0:
                queue.remove(max(queue))            # 최댓값을 삭제할 때는 remove(), max()를 사용한다.
    
    
    if len(queue) == 0:                             # 큐가 비어있으면 [0, 0]으로 반환하고
        answer = [0, 0]
    else:                                           # 비어있지 않으면 [최댓값, 최솟값]으로 반환한다.
        answer = [max(queue), heapq.heappop(queue)]
    

    return answer