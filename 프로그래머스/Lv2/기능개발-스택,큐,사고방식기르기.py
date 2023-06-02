# 접근 방법이 어려웠다. 
# 기능이 100%인 상황이어도 앞의 기능이 100%일 때 같이 배포하기 때문에
# 전체 큐가 빌 때까지 서로 연속된 100%만 빼줘야하는 과정이 어려웠다.

# 내가 구현한 방법은 루프 안에서 pop이 불가능하므로
# 루프 카운트를 미리 선정해서 그 길이 만큼 무조건 반복하면서
# 연속된 다음 값이 100%라 같이 배포할 수 있는 것은 제외대상 리스트에 추가하여
# 위 반복이 끝날 때 제외대상 리스트의 날짜를 기존 총 날짜 리스트에서 지워주어 갱신해주면 문제없이 정상작동이 된다.


def solution(progresses, speeds):
    answer = []
    count_list = []                            # 총 걸리는 날짜 리스트 선언
    
    for i, value in enumerate(progresses):     # 각 progresses에서 100까지 채워지는데 걸리는 날짜를 적용하기 위한 루프
        count = 0                              # 날짜를 초기화

        while value < 100:                     # 진행도가 100%가 될 때까지 반복
            value += speeds[i]                 # 현재 값에 speeds 만큼 더한다.
            count += 1                         # 더했다는 건 하루가 지나므로 카운팅

        count_list.append(count)               # 100%가 되기 위한 총 날짜를 리스트에 넣어주기
    
    
    while count_list:                          # 각 100%가 걸리는 날짜 리스트가 빌 때까지 반복
        temp = count_list.pop(0)               # 제일 앞의 값이 기준이 되어 진행
        result_count = 1                       # 앞의 값을 꺼냈으므로 최종 카운트 1로 초기화하고 시작
        
        loop_count = 0                         # 연속으로 꺼낼 때 반복 과정에서 pop할 수는 없기에 반복 카운트를 총 날짜 리스트의 길이에 맞게 카운팅하며 조회하기로함
        result_list = []                       # 현재 기능에서 다음 연속으로 오는 100% 기능이면 제외시키기 위한 ㄹ스트 따로 선언 
        
        while loop_count != len(count_list):               # 현재 총 날짜 리스트의 길이 만큼 반복하여
            if temp >= count_list[loop_count]:             # 현재 기준 값이 연속되는 다음 값보다 크거나 같으면 
                result_count += 1                          # 같이 배포될 수 있는 것이므로 최종 카운트에 +1
                result_list.append(count_list[loop_count]) # 비교한 것이 같이 배포되는 것이므로 제외대상 리스트에 추가
                loop_count += 1                            # 루프 카운트를 증가시켜 계속 반복 진행

            else:                                          # 만약 위 조건이 아니면 연속으로 배포할 수 없으므로  
                break                                      # 현재 반복을 종료
            
            
        if len(result_list) > 0:                           # 위 반복을 거친 후의 제외 대상 리스트를 조회
            for i in result_list:                          
                if i in count_list:                        # 총 날짜 리스트에서 제외대상 지워주기
                    count_list.remove(i)
            
        answer.append(result_count)                        # 최종 카운팅된 것을 답에 넣어준다.
                    
    return answer