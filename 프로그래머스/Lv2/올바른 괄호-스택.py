# 처음 시도한 풀이 : 처음 스택에 들어온 '('만 비교해도 된다고 착각함
# -> (()) 와 같은 상황일 때의 케이스 측정 불가능

def solution(s):
    answer = True
    stack = []

    for i in s:
        if i == ')':
            if stack and stack[0] == '(':
                stack.pop()
            else:
                answer = False
        else:
            if stack and stack[0] == '(':
                answer = False
            else:
                stack.append(i)
                        
    return answer



# 다시 재풀이
# 스택에는 '('만 넣고 ')'이 올 때 스택의 '('을 지워주면서 
# 모두 조회되었는데도 스택이 비어있지 않으면 짝이 안 맞았다는 것

def solution(s):
    answer = True
    stack = []                        # '('만 넣을 스택
    
    for i in s:
        if i == '(':                  # '('아면 스택에 넣어주기
            stack.append(i)
        elif i == ')':                # ')'이면 스택에서 '(' 지워주기
            if stack:
                stack.pop()
            else:                     # 스택 안이 비어있으면 짝이 안맞으므로 False
                answer = False

    if stack:                         # 위 모두 조회했는데 스택이 비어있지 않으면 짝이 안맞았다는 것이므로 False
        answer = False
    
    return answer