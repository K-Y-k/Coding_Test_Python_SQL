# 내가 푼 방식 = 일부만 맞고 여러 케이스 및 출력초과 등 실패 발생(pop으로 지워주는 과정에서 초과가 발생한 듯하다.)
# 문제의 의도는 한 상자 세트에서 가장 낮은 수를 기준으로 하므로 
# 결국 높은 순으로 정렬하여 높은 수끼리 최대한 한 상자로 넣어줘야 최대 값이 나온다.
# 즉, 정렬을 생각하고 진행하면 쉽게 풀리는 문제! 
# 1. 높은 순으로 정렬하고 
# 2. 한 상자로 들어갈 수 있는 사과만 남기기 위해 나누어 떨어지지 않은 사과들은 낮은 숫자의 사과순으로 제거해주고
# 3. 나누어지는 상자 세트별로 담아질 때마다 (그 상자의 최소값) x (한 상자안의 사과 총개수)로 정답을 쌓아갔다.


def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)         # 1. 높은 순으로 정렬하고 
    
    if len(score) > m:               # 2. 한 상자로 들어갈 수 있는 사과만 남기기 위해 나누어 떨어지지 않은 사과들은
        peace = len(score) % m
    
    if peace != 0:                   #    낮은 숫자의 사과순으로 제거해주었고
        for i in range(peace):
            score.pop()
        
    temp = []                        # 한 상자에 들어가는 세트에 맞게 넣어줄 리스트
    
    for i in score:             
        if len(temp) == m-1:         # 3. 나누어지는 상자 세트별로 담아질 때마다 
            answer += min(temp) * m  #    (그 상자의 최소 값) x (한 상자안의 사과 총개수)로 정답을 쌓아갔다.
            temp = []
        else:
            temp.append(i)
    
    
    return answer



# 슬라이스를 활용해서 다시 푼 방법


def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):           # m의 간격으로 뛰어 넘어
        if len(score[i:i+m]) == m:              # 현재 위치 ~ 현재위치 + m 만큼으로 한 상자의 개수만큼 바로 진행  
            answer += min(score[i:i+m]) * m
    
    
    return answer