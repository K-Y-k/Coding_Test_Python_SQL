# - 큐 + 인덱스 접근 방식
# 큐로 푸는 방식은 인덱스 계산을 잘 처리해야한다.
#  계속 K번째의 위치를 제거해나가기에 기존 제거했던 위치에 + (K-1)을 적용하고 
#  K보다 인덱스가 작아질 때를 대비하여 % len(리스트)도 적용해주어 인덱스가 벗어나지 않게 해야한다. 

# % len(리스트)를 생각하는 것이 어려운 것 같다.


N, K = map(int, input().split())

rotate_table = list(range(1, N+1))                    # 1 ~ N까지라고 했으므로
remove_index = 0                                      # 제거할 인덱스 선언
result = []                                           # 제거된 것을 넣을 최종 결과 리스트 선언

while rotate_table:                                   # 1 ~ N까지 넣은 리스트가 빌 때까지
    remove_index += (K-1)                             # 제거할 인덱스를 K번째 제거하기위한 위치 적용
    remove_index %= len(rotate_table)                 # K보다 작아졌을 경우를 대비해 % len(리스트)로 벗어나지 않게 적용
    result.append(rotate_table.pop(remove_index))     # 위에 적용된 제거할 위치를 꺼내서 최종 결과 리스트에 넣는다.

print('<', end='')
print(', '.join(map(str, result)), end='')            # 문자열 리스트만 join이 가능하므로 map으로 변환후 적용
print('>')



# - 덱 + rotate() 방식
# rotate(-숫자)이면 모든 원소를 숫자만큼 왼쪽으로 회전한다. 
# 이를 활용해 제일 앞의 위치를 K번째 위치로 만들 수 있다.
# 양수이면 오른쪽으로 회전하는데 문제에서는 제거된 다음 위치를 제거해나가는 것인데
# 오른쪽 회전은 문제에서 원하는 위치의 반대로 적용되어 여기서 틀린 연산이다.


from collections import deque

N, K = map(int, input().split())
rotate_table = deque([i for i in range(1, N + 1)])    # = deque(list(range(1, N + 1)))
result = []

while rotate_table:
    rotate_table.rotate(-(K-1))                       # 제일 앞의 위치를 회전하여 K번째 위치로 만들어
    result.append(rotate_table.popleft())             # 제일 앞을 꺼낸 것을 최종 결과 리스트에 넣는다.

print("<" + ", ".join(map(str, result)) + ">")