# 내가 풀어본 방식 : 조합 라이브러리 사용
from itertools import combinations

def solution(numbers):
    answer = []
    
    combination_number = combinations(numbers, 2)     # 해당 배열에 2가지를 뽑는 경우의 수의 조합을 새로 담아둠
    
    for i, j in combination_number:                   # 2개를 뽑은 것을 조회하여
        a = i + j                                   
        if a not in answer:                           # 2개를 더한 값이 답에 없으면 넣기
            answer.append(a)
            
    answer.sort()                                     # 오름차순 정렬
    
    return answer



# 조합 없이 원초적 방식 + set활용
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
                answer.append(numbers[i] + numbers[j])   
                
    answer = sorted(list(set(answer)))                    # set을 활용하여 중복된 값을 지워준다.
    return answer