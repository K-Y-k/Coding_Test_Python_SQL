# 내가 푼 방식 : 효율성 테스트 실패 시간초과
# 무한루프로 각 조건에 충족할 경우 break하여 반환해주었고
# 만약 충족하지 못했으면 정렬을 하고 가장 작은 원소와 2번째 작은 원소를 빼내고 연산하고 넣어주고 카운팅하였다.

def solution(scoville, K):
    answer = 0
    
    while True:
        if len(scoville) == 1 and scoville[0] < K:      # 제약사항으로 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우의 조건처리
            return -1
        
        test_count = 0                                  # 모든 원소가 K이상인지 확인하기 위한 카운트 변수 선언
        
        for i in scoville:                              # 모든 원소가 K이상인지 확인
            if i >= K:
                test_count += 1
                
        if test_count == len(scoville):                 # 모든 원소가 K이상인지 확인
            break
            
        
        for i in scoville:
            if i < K:
                scoville.sort()
                a = scoville.pop(0)
                b = scoville.pop(0)
                scoville.append(a + b*2)
                answer += 1
                break
        
    return answer



# 힙을 사용한 방식
# sort 함수를 매번 사용하게 되면 시간 초과가 난다. 
# 그래서 정렬부분을 해결해주는 파이썬 내장함수 heapq을 사용하면 시간 초과를 해결할 수 있다!

# 기억해야 할 것들!
# 1.주입 받기           : import heapq
#   리스트를 힙으로 변환 : heapq.heapify(힙변수) 
# 2.힙에 넣기           : heapq.heappush(힙변수, 넣을 값) 
# 3.힙에 꺼내오기       : heapq.heappop(힙변수)


import heapq

def solution(scoville, K):
  answer = 0

  heapq.heapify(scoville)                    # 기존 리스트를 힙으로 변환

  if scoville[0] >= K:                       # 힙큐는 항상 정렬되어있기 때문에 제일 앞의 원소가 가장 작은 값이다.
    return answer

  while scoville[0] < K:                     # 가장 작은 원소가 K가 될 때까지 반복
    if len(scoville) == 1:                   
        return -1

    a = heapq.heappop(scoville)              # 가장 앞의 원소를 꺼내오므로 가장 작은 값
    b = heapq.heappop(scoville)              # 가장 앞의 원소를 꺼내오므로 2번째 작은 값

    heapq.heappush(scoville, a + b*2)        # 연산한 값 넣고 자동으로 정렬됨
    answer += 1

  return answer