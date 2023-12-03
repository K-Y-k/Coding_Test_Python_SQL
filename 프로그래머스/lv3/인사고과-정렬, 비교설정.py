# 완호라는 사람의 등수를 구하는 것이므로 첫번째 값이 완호의 성적이므로 
# 기준 값으로 잡은 후

# 근무태도점수 기준으로 내림차순(-)으로 진행하고 만약 같은 값이면 동료평가점수에서 오름차순으로 정렬하면
# scores 리스트에서 뒤에 나온 학생의 첫 번째 점수(a)는 항상 앞에 나온 학생의 첫 번째 점수보다 같거나 작다는 겁니다. 
# 그러면 나중에 탐색하는 학생의 두 번째 점수(b)가 먼저 탐색하는 학생의 두 번째 점수보다 작은 경우가 단 하나라도 있으면 
# 해당 학생보다 두 점수가 높은 학생이 있음이 보장되게 된다.

# 문제에서 완호가 인센티브를 받지 못하는 경우의수인 두 점수 둘 다 높은 사원이 있으면 -1로 반환

def solution(scores):
    answer = 1
    
    target_score1 = scores[0][0]
    target_score2 = scores[0][1]
    
    
    scores.sort(key=lambda x:(-x[0],x[1]))                # 근무태도점수 기준으로 내림차순(-)으로 진행하고 만약 같은 값이면 동료평가점수에서 오름차순으로 정렬
    
    max_score2 = 0
    
    for i, j in scores:
        if i > target_score1 and j > target_score2:       # 문제에서 완호가 인센티브를 받지 못하는 경우의수인 두 점수 둘 다 높은 사원이 있으면 -1로 반환
            return -1
    
        if j >= max_score2:                               # 동료 점수 기준으로 최댓값보다 크면
            max_score2 = j                                # 최댓값을 새로 갱신하고
            
            if i + j > target_score1 + target_score2:     # 만약 둘 다 완호의 점수 보다 크면
                answer += 1                               # 완호보다 순위가 높은 것이므로 정답 카운팅
            
    
    
    return answer