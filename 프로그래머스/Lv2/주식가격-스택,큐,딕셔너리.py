# 내가 푼 방식 : 딕셔너리 활용
# 키는 현재 초, 값은 가격이 떨어지지 않은 횟수를 딕셔너리에 담아서
# 현재 초의 다음 초부터 끝까지 조회하여 현재 초의 가격이 다음 초의 가격보다 작거나 같으면 카운팅하고 계속 다음 원소랑 비교해나가고 
# 현재 초의 가격이 다음 초의 가격보다 크게되면 가격이 떨어진 것이므로 카운팅한 후 더이상 조회를 하지 않는다.

def solution(prices):
    answer = []
    dic = {}
    
    for i, value in enumerate(prices):  
        dic[i] = 0                              # 키는 현재 초, 값은 가격이 떨어지지 않은 횟수를 딕셔너리에 담아서
    
        for j in range(i+1, len(prices)):       # 현재 초의 다음 초부터 끝까지 조회하여
            if value <= prices[j]:              # 현재 초의 가격이 다음 초의 가격보다 작거나 같으면 카운팅하고 계속 다음 원소랑 비교해나가고 
                dic[i] += 1
            else:                               # 현재 초의 가격이 다음 초의 가격보다 크게되면 가격이 떨어진 것이므로 카운팅한 후 더이상 조회를 하지 않는다.
                dic[i] += 1
                break
    
    for i, value in dic.items():                # 최종 카운팅된 딕셔너리의 값을 정답에 넣어준다.
        answer.append(value)
    
    
    return answer



# 큐로 푼 방식
# 리스트로된 가격을 큐로 바꾸고 앞에서 부터 빼오면서 뻬온 값과 다음 원소를 위 방식처럼 비교해나가면서 카운팅
# 앞에서 부터 빼오면서 큐가 빌 때까지 반복하여 하나씩 빼오므로 리스트가 작아지면서 효율성을 증가시킨다.

from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)                           # 큐 선언
    
    while(q):
        price = q.popleft()                     # pop으로 빼와서 list길이가 점점 짧아지면서 for문 효율 증가
        count = 0                               # 카운트 선언 및 초기화
         
        for i in q : 
            if price <= i :
                count += 1
            else:
                count += 1
                break
                
        answer.append(count)                    # 카운팅한 것을 정답에 저장하고 pop으로 빼었으므로 다음 반복은 다음 원소를 기준으로 빼오는 것을 반복하게 됨

    
    return answer