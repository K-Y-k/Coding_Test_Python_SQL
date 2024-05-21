# 출력할 때 절대값 기준으로 작은 값인데 
# 여기서는 음수가 들어갈 수 있어 절대값은 음수랑 양수랑 같은 상황이 있다.

# 이때 더 작은 음수 값으로 출력을 하라고 했으므로
# 튜플을 활용하여 첫항에는 절대값 둘째항에 실제 값을 넣는다.
# 튜플은 첫항의 값 기준으로 정렬되고 만약 값이 같으면 둘째항 값 기준으로 정렬되기 때문이다.

import sys
import heapq

N = int(input())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))       # 튜플을 활용하여 첫항에는 절대값 둘째항에 실제 값을 넣음