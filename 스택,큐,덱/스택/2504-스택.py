# 문제는 이해했지만 어디 기점에서 연산을 처리하는지가 구상이 잘 되지 않았다.
#  또 어려웠던 점은 임시 저장 값인 temp를 1로 초기화한 후 연산을 적용해야한다.

# (, [가 들어올 때 스택에 담고 각각 temp에 2, 3을 곱해준다.
#  ), ]가 들어올 때 스택에 담겨져 있는 (,[을 확인하고 서로 짝이 맞지 않으면 0으로 출력해야하므로 반복을 종료하고 0으로 출력하게 만든다. 



S = input()                                          # (,[, ],)들 입력

stack = []                                           # 담을 스택 선언
temp = 1                                             # 임시 저장 값 1로 초기화
result = 0                                           # 최종 결과 변수 선언

for i, value in enumerate(S):                        # 문자 하나씩 조회
    if value == '(':                                 # ( 이면
        stack.append(value)                          # 스택에 담고
        temp *= 2                                    # 2 적용
        
    elif value == '[':                               # [ 이면 
        stack.append(value)                          # 스택에 넣고
        temp *= 3                                    # 3 적용
        
    elif value == ')':                               # ) 이면 
        if not stack or stack[-1] == '[':            # 스택에 담겨진 것이 없거나 [ 이 있으면
            result = 0                               # 0으로 출력해야하므로 적용
            break                                    # 반복을 종료

        elif S[i-1] == '(':                          # 현재 위치의 앞의 값이 ( 이면
            result += temp                           # 임시 저장한 연산했던 것을 최종 결과에 적용한다.
            
        temp //= 2                                   # 임시 저장 값 초기화 및 담았던 스택에서 제거
        stack.pop()
        
    else:                                            # ] 이면
        if not stack or stack[-1] == '(':            # 스택에 담겨진 것이 없거나 ( 이 있으면
            result = 0                               # 0으로 출력해야하므로 적용
            break                                    # 반복을 종료

        elif S[i-1] == '[':                          # 현재 위치의 앞의 값이 [ 이면
            result += temp                           # 임시 저장한 연산했던 것을 최종 결과에 적용한다.
        
        temp //= 3                                   # 임시 저장 값 초기화 및 담았던 스택에서 제거 
        stack.pop()
        
if stack:                                            # 짝이 맞지않아 스택이 남아있을 경우
    result = 0                                       # 0으로 적용
    
print(result)                                        # 최종 결과 출력