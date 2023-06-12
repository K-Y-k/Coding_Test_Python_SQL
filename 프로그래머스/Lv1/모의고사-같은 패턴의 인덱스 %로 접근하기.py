# 내가 푼 방식
# 1. 10000문제까지라고 했으므로 정해진 패턴에서 x 를 해서 10000개이상의 원소로 초기화한다.
# 2. 문제의 답을 조회할 때 각 패턴의 인덱스와 동일할 때 카운트를 센다.
# 3. 카운트를 센 것에서 최대 값을 지정하고 최대 값과 같은 값인 경우 답에 넣어준다.


def solution(answers):
    answer = []
    
    # 1. 10000문제까지라고 했으므로 정해진 패턴에서 x 를 해서 10000개이상의 원소로 초기화한다.
    one_check = [1,2,3,4,5] * 2000
    two_check = [2,1,2,3,2,4,2,5] * 1250
    three_check = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    one_answer_count = 0
    two_answer_count = 0
    three_answer_count = 0
    
    for i, value in enumerate(answers): # 2. 문제의 답을 조회할 때 각 패턴의 인덱스와 동일할 때 카운트를 센다.
        if one_check[i] == answers[i]:
            one_answer_count += 1
        
        if two_check[i] == answers[i]:
            two_answer_count += 1
            
        if three_check[i] == answers[i]:
            three_answer_count += 1
    
    
    answer_count = []
    answer_count.append(one_answer_count)
    answer_count.append(two_answer_count)
    answer_count.append(three_answer_count)

    # 3. 카운트를 센 것에서 최대 값을 지정하고
    max_count = max(answer_count)

    # 최대 값과 같은 값인 경우 답에 넣어준다.
    for i, value in enumerate(answer_count):
        if value == max_count:
            answer.append(i+1)
    
    
    return answer



# 인덱스를 %로 접근하는 방식


def solution(answers):
    answer = []
    
    one_check = [1,2,3,4,5]                                # 나머지의 인덱스로 접근할 것이기에 지정 패턴까지만 초기화하면 된다. 
    two_check = [2,1,2,3,2,4,2,5] 
    three_check = [3,3,1,1,2,2,4,4,5,5]
    
    one_answer_count = 0
    two_answer_count = 0
    three_answer_count = 0
    
    for i, value in enumerate(answers):
        if one_check[i%len(one_check)] == answers[i]:      # 현재 인덱스에서 해당 배열 인덱스 길이의 나머지 값으로 접근하기
            one_answer_count += 1
        
        if two_check[i%len(one_check)] == answers[i]:
            two_answer_count += 1
            
        if three_check[i%len(one_check)] == answers[i]:
            three_answer_count += 1
    
    print(one_answer_count)
    print(two_answer_count)
    print(three_answer_count)
    
    answer_count = []
    answer_count.append(one_answer_count)
    answer_count.append(two_answer_count)
    answer_count.append(three_answer_count)

    
    max_count = max(answer_count)
    
    for i, value in enumerate(answer_count):
        if value == max_count:
            answer.append(i+1)
    
    
    return answer