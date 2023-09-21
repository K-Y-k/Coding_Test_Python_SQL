# 기존 처음 주어진 큐들로 돌아오는데 걸리는 횟수가 현재 큐길이 x 3이므로
# 이 반복 내에 각 큐의 크기를 비교해서 큰쪽의 큐에서 빼와서 작은쪽의 큐에 넣고 횟수를 카운팅해 나가고
# 같으면 카운팅한 값을 반환하고
# 모든 반복 끝까지 진행해도 같지가 않으면 -1을 반환한다.

from collections import deque

def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)                        # 앞에서 꺼내오는 popleft()를 사용하기 위해 deque로 지정
    queue2 = deque(queue2)

    sum1 = sum(queue1)                            # 미리 선언한 이유는 반복문에서 sum()함수가 무분별하게 들어가면 시간초과가 발생하므로
    sum2 = sum(queue2)
    
    for i in range(len(queue1) * 3):              # 기존 처음 주어진 큐들로 돌아오는데 걸리는 횟수가 현재 큐길이 x 3이다.
        # 각 큐의 크기를 비교해서 큰쪽의 큐에서 빼와서 작은쪽의 큐에 넣고 횟수를 카운팅해 나가고
        if sum1 > sum2:
            sum1 -= queue1[0]                     # 이렇게 하나씩 값을 빼주고 더해주는 작업으로 효율성을 높인다.
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        else:                                    # 같으면 카운팅한 값을 반환하고
            return answer
        
        answer += 1


    return -1                                    # 모든 반복 끝까지 진행해도 같지가 않으면 -1을 반환한다.