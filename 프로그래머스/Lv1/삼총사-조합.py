# 내가 푼 방식
# 배열에서 3명을 뽑아서 합이 0일 때 삼총사라는 것이므로
# 조합 모듈을 사용하여 3명을 뽑은 모든 경우의 값들을 저장한 것을
# 모두 조회하여 합이 0이면 카운팅해주었다.
 

from itertools import combinations

def solution(number):
    answer = 0
    
    c = combinations(number, 3)     # 조합 모듈을 사용하여 3명을 뽑은 모든 경우의 값들을 저장한 것을
    
    for i in c:                     # 모두 조회하여
        if sum(i) == 0:             # 합이 0이면 카운팅해주었다.
            answer += 1
    
    return answer