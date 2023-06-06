# 딕셔너리를 사용하여 카운팅하고 
# 카운팅한 것이 최대 값이면 카운트 리스트에 넣어서 출력했다.


def solution(array):
    answer = 0

    array_dic = {}                            # 카운팅할 딕셔너리 선언
    
    for i in array:                           # 카운팅한 것을 딕셔너리에 넣기
        if i not in array_dic:
            array_dic[i] = 1
        else:
            array_dic[i] += 1
            
            
    count_list = []                           # 최빈 값만 넣기 위한 리스트 선언
    for key, value in array_dic.items():      # 최대 값 
        if value == max(array_dic.values()):  # 현재 카운팅 값이 최대 값이면 최빈 값이므로 
            count_list.append(key)            # 최빈 값 리스트에 넣어준다.
            
    
    if len(count_list) > 1:                   # 최빈 값 리스트에 여러 개가 있으면
        answer = -1                           # -1로 출력하게 넣기
    else:                                     # 한 개이면
        answer = count_list[0]                # 최빈 값으로 출력하게 넣기
    
    return answer