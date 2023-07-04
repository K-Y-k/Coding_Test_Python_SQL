# 내가 푼 방식
# 스킬이 찍힌 상태인지 구별하기 위한 딕셔너리를 선언하였고
# 스킬트리의 스킬이 온 경우 이전 스킬이 찍혔는지 검사하여 이전 단계 스킬이 찍혀있으면 딕셔너리 값을 체크해주고
# 모두 조회가 된경우 for else문에서 정상 스킬이 찍힌 것으로 카운팅 처리하였다. 

def solution(skill, skill_trees):
    answer = 0
    skill_dic = {}                                              # 스킬이 찍힌 상태인지 구별하기 위한 딕셔너리를 선언
            
        
    for i in skill_trees:
        for s in skill:                                         # 딕셔너리에 처음에 스킬이 찍히지 않은 상태로 초기화
            skill_dic[s] = 0

        for j in i:
            if j in skill:                                      # 스킬트리의 스킬인 경우
                if skill.index(j) == 0:                         # 첫 인덱스인 경우면 무조건 정상이므로 찍어주었다.
                    skill_dic[j] = 1
                elif skill.index(j) > 0:                        # 그외 인덱스의 경우면 이전 인덱스의 스킬이 찍혀있는지 조회하고 
                    if skill_dic[skill[skill.index(j)-1]] == 0: # 이전 인덱스의 스킬이 찍혀있지 않으면 더이상 이 스킬 리스트는 의미가 없어 break 
                        break
                    else:                                       # 이전 인덱스의 스킬이 찍혀있으면 현재 인덱스 스킬도 찍어주었다.
                        skill_dic[j] = 1
        else:                                                   # 위 반복이 모두 된 경우 for else문이 작동하여 정상적으로 스킬이 찍힌 것이므로 정답에 카운팅
            answer += 1
                        
    
    return answer



# 효율적인 방식
# 스킬트리에 해당되는 스킬은 스킬 리스트 문자열에 추가하여
# 모두 넣어진 최종 스킬 리스트가 스킬트리랑 같으면 카운팅 처리

def solution(skill, skill_trees):
    answer = 0
        
    for i in skill_trees:
        skill_list = ''
        
        for j in i:                                  # 스킬트리의 스킬인 경우
            if j in skill:                           # 스킬트리에 해당되는 스킬은 스킬 리스트 문자열에 추가하여
                skill_list += j
                
        if skill[0:len(skill_list)] == skill_list:   # 모두 넣어진 최종 스킬 리스트가 스킬트리랑 같으면 카운팅 처리
            answer += 1
    
    
    return answer