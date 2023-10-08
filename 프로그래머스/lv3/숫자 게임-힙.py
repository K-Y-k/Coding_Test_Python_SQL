# 내가 시도한 방식 = 시간초과
# 문제의 주어지는 숫자의 범위가 넓어 2중 루프 + 그 내부의 remove()를 사용하면 시간초과가 날 수 밖에 없다. 

def solution(A, B):
    answer = 0

    for i in A:
        for j in range(i+1, max(B)+1):
            if j in B:
                answer += 1
                B.remove(j)


    return answer



# 힙 활용 방식
# 문제의 요점은 결국 A의 값은 B의 값 중 최대한 A의 값보다 가까우면서 커야하므로
# 최소순으로 정렬한 후 A의 값과 B의 값을 순차적으로 올려가며 비교하면 된다.

import heapq

def solution(A, B):
    answer = 0

    heapq.heapify(A)                 # 힙으로 적용하여 자동으로 최소순으로 정렬한 후
    heapq.heapify(B)                 

    while B:                         # B의 값이 빌 때까지
        A_val = heapq.heappop(A)     # A의 기준 값을 꺼내고

        while B:                     # 해당 A와 비교할 B를
            B_val = heapq.heappop(B) # 하나씩 꺼내가며

            if B_val > A_val:        # 값이 클 때까지 비교한다. 
                answer += 1          # 어차피 최대한 가까운 값으로 비교하는 것이므로 A의 값이 남게 되어도 이게 최대로 점수를 내는 값이 된다.
                break


    return answer