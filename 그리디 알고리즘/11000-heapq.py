import sys
import heapq                                            # 힙 우선순위 큐 활용

N = int(input())

conference_time = []                                    # 회의 시간들을 넣을 리스트
result = []                                             # 힙 우선순위 큐를 넣을 리스트


for _ in range(N):                                      # 입력한 값 만큼 강의의 시작 시간, 끝나는 시간 입력 반복
    start, end = map(int, sys.stdin.readline().split()) # 반복문에서  sys.stdin.readline() 사용(시간초과방지)
    conference_time.append([start, end])

conference_time.sort(key=lambda x: x[0])                # 시작시간 기준으로 오름차순 정렬

heapq.heappush(result, conference_time[0][1])           # 첫번째 강의가 끝나는 시간을 넣어서 강의실 하나 개설
  

for i in range(1, N):                                   # 첫번째는 위에 했으므로 두번째부터 루프를 돌림
    if result[0] > conference_time[i][0]:               # 새로 들어가는 시작시간이 개설된 강의실의 끝나는 시간보다 클 경우 
        heapq.heappush(result, conference_time[i][1])   # 강의실을 새로 만들어야하기에 큐에 새로 넣어 개설

    else:                                               # 새로 들어가는 시작시간이 등록된 끝나는 시간보다 같거나 작으면
        heapq.heappop(result)                           # 같은 강의실로 배정이 가능하여 기존 등록시간을 제거하고
        heapq.heappush(result, conference_time[i][1])   # 끝나는 시간을 새로 들어온 것으로 새로 갱신한다.


print(len(result))                                      # 넣어진 큐의 총 개수 출력하면 강의실이 개설된 총 개수가 반환