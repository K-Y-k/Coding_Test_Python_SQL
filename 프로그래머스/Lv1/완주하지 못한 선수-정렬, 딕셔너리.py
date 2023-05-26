# 정렬 방식: 하나의 주자만 들어오지 못하므로 completion이 전체 참여자보다 1작으므로
#            둘 다 정렬을 해준 후 같은 인덱스끼리 비교해 나가면 한명의 완주하지 못한 자를 찾을 수 있다. 

def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    for i, value in enumerate(completion):
        if participant[i] != completion[i]:          # 같은 위치의 인덱스끼리 비교해서 다르면 
            answer = participant[i]                  # 완주 못한 자이므로 추가
    
    if answer == '':                                 # 완주자 리스트는 전체 완주자 리스트보다 1명 없으므로 전체완주자-1만큼 즉, 모두 조회해도 answer에 지정된 것이 없으면
        answer = participant[len(participant)-1]     # 전체 완주자의 마지막 항이 완주 못한 자이므로 적용
    
    return answer



# 딕셔너리를 사용한 방식: 전체 참여자를 하나씩 딕셔너리에 카운팅해 놓은 것을
#                        완주자를 조회할 때 하나씩 카운팅을 감소시켜서 최종 카운팅이 1인 것이 완주 못한 자가 나오게함 

def solution(participant, completion):
    answer = ''

    hashDic = {}
    
    for i in participant:                           # 전체 참여자를 하나씩 딕셔너리에 카운팅해 놓음
        if i in hashDic:
            hashDic[i] += 1
        else:
            hashDic[i] = 1
            
    for i in completion:                            # 완주자를 조회하면서 딕셔너리에 있으면
        if i in hashDic:                 
            hashDic[i] -= 1                         # -1 카운팅
            
    for i in hashDic:                               # 딕셔너리를 조회하여
        if hashDic[i] == 1:                         # 1인 값이 결국 완주하지 못한 자이므로
            answer = i                              # 답에 적용

    return answer