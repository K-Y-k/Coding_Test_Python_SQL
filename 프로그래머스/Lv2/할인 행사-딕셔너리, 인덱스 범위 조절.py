# 내가 푼 방식
# 1. 딕셔너리에 담아서 
# 2. 10일 연속으로 하루씩 이동하여 조회하여 
# 3. 원하는 물품이 모두 충족된 경우 정답에 카운팅 해주엇다.


def solution(want, number, discount):
    answer = 0
    count = 0
        
    while count < len(discount)-9:
        temp_dic = {}                             # 1. 딕셔너리에 담기
        for i in range(len(want)):
            if want[i] not in temp_dic:
                temp_dic[want[i]] = number[i]
                
        for i in range(count, count+10):          # 2. 10일 연속으로 하루씩 이동하여 조회하여 딕셔너리에 해당하는 값은 -해주기
            if discount[i] in temp_dic:
                temp_dic[discount[i]] -= 1
        
        
        temp_count = 0
        for i in temp_dic:                        # 딕셔너리의 모든 값이 0인지 조회하기
            if temp_dic[i] == 0:
                temp_count += 1
                
        if temp_count == len(want):               # 3. 원하는 물품이 모두 충족된 경우 정답에 카운팅 해주기
            answer += 1
        
        count += 1

    
    return answer