# 내가 푼 방식
# deque의 rotate함수로 회전시켜서 동일한 문자가 되면 회전한 횟수를 정답에 넣어주고
# 문자열 길이만큼 반복해도 같은 문자가 되지 않으면 -1을 넣었다. 

from collections import deque

def solution(A, B):
    answer = 0                         # 초깃 값을 서로 같을 때의 결과 값으로 초기화
    
    if A != B:                         # A와 B가 다르면 회전 진행
        q = deque(A)

        for i in range(1, len(B)+1):   # deque의 rotate함수로 회전시켜서
            q.rotate()
            temp = ''

            for j in q:
                temp += j

            if temp == B:              # 동일한 문자가 되면 회전한 횟수를 정답에 넣어주고
                answer = i
                break
        else:                          # 문자열 길이만큼 반복해도 같은 문자가 되지 않으면 -1을 넣었다. 
            answer = -1
        
    return answer



# 튜플 슬라이스 방식
# 기존 값의 끝 값을 앞에 넣고 기존 값의 첫항부터 끝의 앞까지를 뒤에 넣으면 회전하는 형태로 표현가능하다.

def solution(A, B):
    answer = 0
    
    if A != B:
        for i in range(1, len(A)+1):
            A = A[-1] + A[:-1]          # 기존 값의 끝 값을 앞에 넣고 기존 값의 첫항부터 끝의 앞까지를 뒤에 넣으면 회전하는 형태로 표현가능하다.
 
            if A == B:
                answer = i
                break
        else:
            answer = -1
    

    return answer