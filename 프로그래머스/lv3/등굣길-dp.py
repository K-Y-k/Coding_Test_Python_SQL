# 내가 시도한 방식 = 연산처리 정상적으로 안됨
# 행렬 끝 라인들은 모두 1의 경우의 수이므로 미리 초기화 했고
# 웅덩이는 False로 구분했지만
# False 때문에 연산적용이 잘 안되는 것 같다.

def solution(m, n, puddles):
    answer = 0
    
    d = [[0] * (m+1) for _ in range(n+1)]
    
    # 행과 열 끝 라인들은 모두 1의 경우의 수이므로 미리 초기화 했고
    for i in range(1, m+1):
        d[1][i] = 1
    
    for i in range(1, n+1):
        d[i][1] = 1
    
    # 웅덩이는 False로 구분
    for i, j in puddles:
        d[j][i] = False    
    
    
    for i in range(2, n+1):
        for j in range(2, m+1):
            if d[i][j] == False or d[i-1][j] == False and d[i][j-1] == False:
                continue
            
            if d[i-1][j] == False:
                d[i][j] = d[i][j-1]
            elif d[i][j-1] == False:
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = (d[i-1][j] + d[i][j-1]) % 1000000007
    
    answer = d[n][m]
    
    return answer


# 웅덩이를 False 대신 -1로 구분짓고 적용한 방식
# 웅덩이를 -1로 적용하고 웅덩이인 경우 다음 연산에 지장되지 않게 0으로 바꿔주니 정상적으로 처리되었다.

def solution(m, n, puddles):
    answer = 0
    
    d = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, m+1):
        d[1][i] = 1
    
    for i in range(1, n+1):
        d[i][1] = 1
    
    for i, j in puddles:
        d[j][i] = -1 
    
    
    for i in range(2, n+1):
        for j in range(2, m+1):
            if d[i][j] == -1:
                d[i][j] = 0
                continue
            
            d[i][j] = (d[i-1][j] + d[i][j-1]) % 1000000007
    
    
    answer = d[n][m]
    
    return answer