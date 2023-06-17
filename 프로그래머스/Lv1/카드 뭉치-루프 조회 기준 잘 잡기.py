# 내가 푼 방식 = 일부 테스트케이스 인덱스 초과 에러
# 각 cards1, cards2의 위치의 값과 goal의 위치의 값이 같으면 temp에 넣는 과정으로 했지만 일부 테스트케이스 실패


def solution(cards1, cards2, goal):
    answer = ''
    temp = []
    
    for i in range(0, len(max(cards1, cards2))):
        if i <= len(cards1)-1 and cards1[i] not in temp and cards1[i] == goal[len(temp)]:
            temp.append(cards1[i])
            
            for j in range(i+1, len(cards1)):
                if cards1[j] == goal[len(temp)]:
                    temp.append(cards1[j])
        
        if i <= len(cards2)-1 and cards2[i] not in temp and cards2[i] == goal[len(temp)]:
            temp.append(cards2[i])
            
            for j in range(i+1, len(cards2)):
                if cards2[j] == goal[len(temp)]:
                    temp.append(cards2[j])
    
    if goal == temp:
        answer = 'Yes'
    else:
        answer = 'No'
    
    return answer



# goal을 기준으로 접근해서 cards1과 cards2를 비교하는 방식
# 결국 goal의 위치의 단어를 기준으로 그 위치의 인덱스의 카드뭉치를 비교해나가면 순차적으로 진행이 된다.


def solution(cards1, cards2, goal):
    answer = ''
    temp = []                                                       # goal과 비교할 배열 선언  
    
    cards1_idx = 0                                                  # 각 카드 뭉치의 인덱스를 조정해주기 위해 선언
    cards2_idx = 0
    
    for word in goal:                                               # 목표를 기준으로 조회
        if cards1_idx < len(cards1) and cards1[cards1_idx] == word: # 인덱스가 카드 뭉치의 길이보다 초과하지 않는지 검사도 필요
            temp.append(word)
            cards1_idx += 1
        
        if cards2_idx < len(cards2) and cards2[cards2_idx] == word:
            temp.append(word)
            cards2_idx += 1
            
    
    if goal == temp:
        answer = 'Yes'
    else:
        answer = 'No'

    
    return answer