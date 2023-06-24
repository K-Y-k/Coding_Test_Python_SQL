# 내가 푼 방식
# 최소 종류로 담고 싶으므로 딕셔너리에 넣고 
# 종류에 담긴 value를 내림차순으로 정렬하여 k개 만큼까지 차례로 담겨서 그 담긴 종류의 수를 반환햇다.


def solution(k, tangerine):
    answer = 0                        # 담긴 종류의 수 변수 선언 
    tagerine_dic = {}
    
    for i in tangerine:               # 딕셔너리에 넣기
        if i not in tagerine_dic:
            tagerine_dic[i] = 1
        else:
            tagerine_dic[i] += 1 
            
    
    count = 0                                                                            # 담긴 종류의 수 변수 선언 
    tagerine_dic = dict(sorted(tagerine_dic.items(), key=lambda x:x[1], reverse=True))   # value 값 기준의 내림차순으로 정렬
    
    for i, value in enumerate(tagerine_dic):                                             
        if count + tagerine_dic[value] < k:                                               # value값을 더한 것이 k개보다 작으면 더해주고 그 종류를 카운팅
            count += tagerine_dic[value]
            answer += 1
        elif count + tagerine_dic[value] >= k:                                            # value값을 더한 것이 k개보다 같거나 크면 더해주고 그 종류를 카운팅하고 반복 종료
            count += tagerine_dic[value]
            answer += 1
            break


    return answer