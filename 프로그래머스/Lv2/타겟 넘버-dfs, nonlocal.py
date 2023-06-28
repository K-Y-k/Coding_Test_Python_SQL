# 문제가 각 원소의 +와 -의 경우로 나뉘어지므로 각 원소의 각 2가지 케이스를 뻗은 것을 dfs로 탐색하여 합산하면서 
# 마지막 항일 때 target을 만족할 때 정답에 카운팅 해준다.


def solution(numbers, target):
    def dfs(idx, sum_total):
        nonlocal total_idx                         # nonlocal은 'local이 아니다'고 선언해주는 키워드다. 
        nonlocal count                             # 즉 상위 함수의 변수를 참조한다고 미리 선언한다는 것이다. 

        if idx == total_idx - 1:                   # 마지막 항일 때 target을 만족할 때 정답에 카운팅 해준다.
            if sum_total == target:
                count += 1
            return
        else:                                      # 마지막 항이 아닐 경우 다음 원소의 +, -의 각 케이스를 재귀호출
            dfs(idx+1, sum_total + numbers[idx+1])
            dfs(idx+1, sum_total - numbers[idx+1])
    
    total_idx = len(numbers)                       # 마지막 항을 확인할 때의 변수 선언
    count = 0                                      # target을 만족한 경우 카운팅할 변수 선언
    
    dfs(-1,0)                                      # 첫 항부터 +, -로 나누어서 시작하라면 idx를 -1부터 시작 

    return count