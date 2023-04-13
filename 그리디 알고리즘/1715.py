import sys       				                          # sys.stdin.readline()을 사용하기 위해 선언
import heapq 				                              # 힙큐를 사용하기 위해 선언

N = int(input()) 				                          # 카드 묶음 개수 선언
card_list = []    				                          # 카드 묶음을 담을 리스트 선언
result = 0        				                          # 결과 변수 선언

for _ in range(N):                                        # 지정한 만큼 카드 묶음 값 넣기
    heapq.heappush(card_list, int(sys.stdin.readline()))  # heappush는 오름차순으로 넣어준다.

if len(card_list) == 1:                                   # 카드 묶음의 개수가 1개이면 2묶음으로 더하지 못하므로 0으로 출력
    print(0)

else:    					                              # 카드 묶음의 개수가 2개이상이면
    while len(card_list) > 1: 			                  # 카드 묶음이 1개이하로 남을 때까지 반복
        temp1 = heapq.heappop(card_list) 		          # heappop은 가장 작은 카드 묶음 값부터 가져옴
        temp2 = heapq.heappop(card_list)		          # 그 다음으로 낮은 카드 묶음 값 가져옴

        plus = temp1 + temp2  			                  # 2묶음을 더하여 결과에 합산
        result += plus

        heapq.heappush(card_list, plus)  		          # 2묶음을 더할 수 없을 때 2묶음 더한 값 + 나머지 값의 총 합이므로 더 했던 값을 다시 넣는 것이다.

    print(result)    				                      # 결과 출력