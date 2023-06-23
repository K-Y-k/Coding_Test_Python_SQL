# 내가 푼 방식 : 점화식이 틀렸다..
# 방법의 수를 구하라고 해서 dp를 떠올렸고 dp로 접근했다.
# 일부 경우의 수를 파악하고 규칙을 찾았는데 사실 잘못된 규칙을 찾은 것... 

def solution(n):
    answer = 0
    
    d = [0] * 2001
    d[1] = 1
    d[2] = 2
    
    for i in range(3, len(d)):
        d[i] = d[i-1] + i-2
    
    answer = d[n] % 1234567
    
    return answer



# 잘된 점화식

def solution(n):
    answer = 0
    
    d = [0] * 2001
    d[1] = 1
    d[2] = 2
    
    for i in range(3, len(d)):
        d[i] = d[i-2] + d[i-1]
    
    answer = d[n] % 1234567
    
    return answer