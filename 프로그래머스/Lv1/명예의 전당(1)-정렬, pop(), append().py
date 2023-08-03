# 내가 푼 방식
# 명예의 전당 리스트의 길이가 k의 길이보다 작으면 그냥 넣고
# k의 길이와 같으면 제일 앞의 값과 현재 점수와 비교하여 현재 점수가 크면 제일 앞의 값을 지우고 새로 넣어준다.
# 제일 앞의 값이 가장 작은 값이 되도록 마지막에는 정렬처리를 해준 후에 가장 작은 값을 정답에 넣어준다.
 
def solution(k, score):
    answer = []
    score_list = []                       # 명예의 전당 리스트
    
    for i in score:
        if len(score_list) < k:           # 명예의 전당 리스트의 길이가 k의 길이보다 작으면
            score_list.append(i)          # 그냥 넣고

        elif len(score_list) == k:        # 명예의 전당 리스트의 길이가 k의 길이와 같으면 
            if i > score_list[0]:         # 제일 앞의 값과 현재 점수와 비교하여 현재 점수가 크면
                score_list.pop(0)         # 제일 앞의 값을 지우고
                score_list.append(i)      # 새로 넣어준다.
        
        score_list.sort()                 # 제일 앞의 값이 가장 작은 값이 되도록 마지막에는 정렬처리를 해준 후에
        answer.append(score_list[0])      # 가장 작은 값을 정답에 넣어준다.
        
        
    return answer



# remove()와 min()으로 사용한 방식

def solution(k, score):
    answer = []
    score_list = []

    for i in score:
        if len(score_list) < k:           
            score_list.append(i) 

        elif len(score_list) == k:
            if i > min(score_list):
                score_list.remove(min(score_list))
                score_list.append(i)

        answer.append(min(score_list))


    return answer