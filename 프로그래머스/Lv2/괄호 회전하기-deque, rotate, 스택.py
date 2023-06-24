# 내가 푼 방식
# 오른쪽으로 돌려가면서 스택에 넣어서 괄호가 모두 매칭이 되는지 비교해서 
# 매칭된 경우 스택에서 제거하고 매칭된 수를 중가시킨다.
# 최종 스택이 비어있고 매칭된 개수가 맞으면 모두 괄호가 매칭이 된 것이므로 카운트를 세고 반환한다.

# 주의점 
# 테스트 케이스 하나가 실패했는데 그 이유는 
# 아래 for문의 else문으로 스택이 비어있는데 }, ), ]이 들어오면 매칭되는 것이 없는 케이스가 있는데 그 처리를 못했기 때문이었다.


from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    
    a = 1
    while a < len(s)+1:
        stack = []
        
        condition = len(s) // 2                             # 짝의 개수 선언
        temp = 0                                            # 현재까지 매칭(짝)된 개수 선언
        
        if a > 1:
            s.rotate(-1)
        
        for i in s:
            if i == '{' or i == '(' or i == '[':            # {, (, [은 스택에 무조건 넣는다.
                stack.append(i)
            elif i == '}' and stack and stack[-1] == '{':   # 매칭된 경우 스택에서 제거하고 매칭된 수를 중가시킨다.
                stack.pop()
                temp += 1
            elif i == ')'and stack and stack[-1] == '(':
                stack.pop()
                temp += 1
            elif i == ']' and stack and stack[-1] == '[':
                stack.pop()
                temp += 1
            else:                                           # 스택이 비어있는데 }, ), ]이 들어오면 매칭되는 것이 없으므로 이번 반복에서 카운팅을 제외하기 위한 조건
                temp = -1
                break
        
        
        if temp == condition and len(stack) == 0:          # 최종 스택이 비어있고 매칭된 개수가 맞으면 모두 괄호가 매칭이 된 것이므로 카운팅한다.
            answer += 1
                        
        
        a += 1
    
    return answer