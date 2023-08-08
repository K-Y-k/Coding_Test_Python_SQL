# 내가 시도한 방식 = 일부 테스트 케이스 시간 초과
# 기준을 문자열로 저장해두고
# 하나씩 쌓아가면서 기준 값이 있으면 해당 기준 값을 빈값으로 교체하고 카운팅하는 방식을 고안했지만
# replace함수는 문자열이 만약 길 때 모두를 조회해야하기에 시간 초과가 발생하는 것이다.

def solution(ingredient):
    answer = 0
    
    standard = '1231'                            # 기준을 문자열로 저장해두고
    tmp = ''
    
    for x in ingredient:
        tmp += str(x)                            # 하나씩 쌓아가면서
        
        if standard in tmp:                      # 기준 값이 있으면
            tmp = tmp.replace(standard, '',1)    # 해당 기준 값을 빈값으로 교체하고
            answer += 1                          # 카운팅

            
    return answer



# 스택 방식을 이용해 4번 pop()으로 빠르게 연산하는 방식
# 스택을 쌓을 때 제일 최근 4개의 값이 [1,2,3,1]이면 4번 pop()하여 제거하고 카운팅

def solution(ingredient):
    answer = 0
    
    standard = [1,2,3,1]
    stack = []
    
    for x in ingredient:
        stack.append(x)
        
        if stack[-4:] == standard:            # 스택을 쌓을 때 제일 최근 4개의 값이 [1,2,3,1]이면
            for _ in range(4):                # 4번 pop()하여 제거하고
                stack.pop()
            
            answer += 1                       # 카운팅

            
    return answer