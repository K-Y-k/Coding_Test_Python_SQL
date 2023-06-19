# 문제에서 출력해야 하는 값은 [변환된 횟수, 0을 제거한 개수]이므로 각 카운트를 선언하고
# 최종 나오는 값이 '1'이므로 '1'이 될 때까지 변환을 반복하면서 변환 개수를 카운팅하고 
# 0을 뺄 때 0을 제거한 개수를 카운팅하면서 이진 변환을 진행한다.


def solution(s):
    answer = []

    # 각 카운트를 선언
    count = 0
    zero_count = 0
    
    while len(s) > 1:                   # 최종 나오는 값이 '1'이므로 '1'이 될 때까지 변환을 반복하면서
        count += 1                      # 변환 개수를 카운팅하고 
        temp = ""                       # 0을 뺀 값을 일단 넣어둘 리스트
        
        for i in s:                     # 1만 temp에 넣기 위한 작업
            if i == '1':
                temp += i
            else:                       # 0일 때 0을 뺀 개수를 카운팅해주기
                zero_count += 1
        
        s = format(len(temp), 'b')      # 1만 들어있는 temp를 2진법으로 변환
        # s = bin(len(temp))[2:]
        

    # 위 작업을 모두 한 후의 카운팅을 정답에 넣기     
    answer.append(count)               
    answer.append(zero_count)

    
    return answer