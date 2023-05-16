# 중요도에 따라 프린트가 출력되는데 현재 프린트 하려는 것이 중요도가 가장 높아야 출력이 되고
# 중요도 높은 것이 뒤에 있다면 현재 출력하려는 것을 뒤로 미룬다.

# 이렇게 뒤로 다시 미루기에 문제에서 원하는 처음 주어진 인덱스의 종이가 몇번째에 인쇄되는지이므로 
# 처음 주어졌던 인덱스의 위치를 정확히 알 수 있게 따로 선언해줘야한다.

# 즉, 중요도 리스트가 빌 때까지 위 작업을 반복하고
# 몇번째인지 궁금한 것의 인덱스와 동일하면 그 값을 출력하면된다.

# eque일 때는 popleft()로 가장 앞의 것을 가져올 수 있고
# 일반 배열 리스트는 pop(0)으로 가장 앞의 것을 가져올 수 있다.
# 이를 비교하기 위해 important_list는 일반 배열로 important_list_index는 deque로 각 방식을 적용해보았다.


from collections import deque
import sys

T = int(input())

for _ in range(T):
    N, index = map(int, sys.stdin.readline().rstrip().split())             # 종이 개수와 몇번째에 인쇄되는지 궁금한 인덱스 입력
    
    important_list = list(map(int, sys.stdin.readline().rstrip().split())) # 리스트 배열로 선언한 중요도 리스트
    important_list_index = deque(list(range(N)))                           # 큐로 선언한 중요도 리스트의 인덱스

    count = 0                                                              # 지금까지 인쇄된 숫자 초기화
    
    while important_list:                                                  # 중요도 리스트가 모두 인쇄되어 빌 때까지
        if important_list[0] == max(important_list):                       # 제일 앞에 있는 것이 가장 큰 중요도 값이면
            count += 1                                                     # 인쇄하므로 인쇄 숫자를 카운팅하고
            important_list.pop(0)                                          # 중요도 리스트에서 제거해주고
            pop_index = important_list_index.popleft()                     # 중요도 리스트의 인덱스에서도 제거해준다.
            
            if pop_index == index:                                         # 현재 인쇄한 인덱스가 궁금한 인덱스 입력 값과 같다면
                print(count)                                               # 지금까지 카운팅한 인쇄 숫자를 출력하고
                break                                                      # 반복 종료

        else:                                                              # 현재 앞에 있는 것이 중요도가 제일 큰 것이 아니면
            important_list.append(important_list.pop(0))                   # 중요도 리스트와 중요도 리스트 인덱스를 제일 뒤로 미룬다.
            important_list_index.append(important_list_index.popleft())