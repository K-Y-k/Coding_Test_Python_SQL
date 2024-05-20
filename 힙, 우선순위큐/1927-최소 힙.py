# 입력 x가 0 이외의 자연수이면 배열에 x값을 넣는다.
# 입력 x가 0이면 배열에 가장 작은 값을 출력하면서 제거하라고 했으므로 최소힙으로 가장 작은 값을 꺼내오게 했다.

import sys
import heapq

N = int(input())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:                            # 입력 x가 0이면 배열에 가장 작은 값을 출력하면서 제거하라고 했으므로
        if len(heap) > 0:
            print(heapq.heappop(heap))    # 최소힙으로 가장 작은 값을 꺼내오게 했다.
        else:
            print(0)
    else:                                 # 입력 x가 0 이외의 자연수이면 배열에 x값을 넣는다.
        heapq.heappush(heap, x)