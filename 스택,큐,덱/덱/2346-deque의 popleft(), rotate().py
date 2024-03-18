# 내가 푼 방식
# 출력은 현재 인덱스를 넣고 
# 이동은 현재 값을 기준으로 이동해야하므로 인덱스와 값이 동시에 필요하다.
# 그래서 인덱스와 값을 각각 선언했고
# 처음에 현재 인덱스와 이동할 값을 빼와서 
# 현재 인덱스는 정답에 넣어주고
# 현재 값만큼 이동처리해준다.
# 하지만 빼왔으므로 한칸이 이미 이동된 상태인 것을 유의하여 이동할 때 1칸을 유의하여 적용해줘야 한다.

# 부족했던 점
# 1) 인덱스와 값을 하나로 묶어서 하고 싶었지만 방도가 생각이 안나서 인덱스와 값을 각각 따로 생성
# 2) 처음에 값을 pop()으로 앞의 값을 빼면 이미 앞으로 한칸 전진된 상태가 되므로
#    값이 마이너스 일 때는 오른쪽으로 한칸 이동된 상태이므로 원래 값만큼 이동한다.

from collections import deque

N = int(input())

balloon_val = deque(list(map(int, input().split())))
balloon_idx = deque([i for i in range(1, N+1)])

answer = []

for _ in range(N):
    move = balloon_val[0]
    balloon_val.popleft()
    answer.append(balloon_idx.popleft())

    if move > 0:
        balloon_val.rotate(-move+1)
        balloon_idx.rotate(-move+1)
    else:
        balloon_val.rotate(-move)
        balloon_idx.rotate(-move)


print(' '.join(map(str, answer)))



# 인덱스와 값을 하나의 튜플로 묶는 방식
# enumerate로 인덱스와 값을 묶을 수 있었다.
# 단 enumerate의 인덱스는 0부터 시작이므로 정답에 인덱스를 넣어줄 때 +1 해주기

# enumerate는 파이썬의 내장 함수로,
# 순회 가능한(iterable) 자료형(리스트, 튜플, 문자열 등)을 입력으로 받아 각 요소를 순회하면서 인덱스와 함께 요소를 반환한다. 
# 이를 통해 반복문 내에서 요소의 값과 해당 요소의 인덱스를 동시에 사용할 수 있게 해준다.

from collections import deque

N = int(input())

balloon_q = deque(enumerate(map(int, input().split())))              # enumerate로 인덱스와 값을 묶을 수 있었다.

answer = []

for _ in range(N):
    idx, move = balloon_q.popleft()
    answer.append(idx+1)                                             # 단 enumerate의 인덱스는 0부터 시작이므로 정답에 인덱스를 넣어줄 때 +1 해주기

    if move > 0:
        balloon_q.rotate(-move+1)
    else:
        balloon_q.rotate(-move)


print(' '.join(map(str, answer)))
