# 이 문제에서의 조건을 하나씩 파악한 후 
# 각 조건을 만족하는지 확인하면 된다.
# 조건 1) 가로 >= 세로
#      2) 카펫 총 개수 = brwon + yellow
#      3) brown = 2*가로 + 2*세로 - 4

# 내가 푼 방식 : 2중루프로 인한 일부 테스트케이스 시간초과 발생

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(1, total+1):
        for j in range(1, total+1):
            if i >= j:
                if 2*i+2*j-4 == brown:
                    if i*j == total:
                        answer.append(i)
                        answer.append(j)
    
    return answer



# 1차원 루프로 푼 방식 : 총 개수(brown+yellow)에서 나눈 몫으로 먼저 접근하기

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(1, total+1):
        j = total // i
        
        if i*j == total:
            if i >= j:
                if 2*i+2*j-4 == brown:
                    answer.append(i)
                    answer.append(j)
    
    return answer