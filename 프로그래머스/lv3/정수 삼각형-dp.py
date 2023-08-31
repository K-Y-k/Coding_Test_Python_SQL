# 정삼각형 형태로 숫자들이 배치가 되어 있는데
# 대각선으로 오른쪽, 왼쪽 값들을 더해가므로 각 열에서 현재 위치와 바로 옆의 위치의 값들을 각 최대 값으로 최신화 해가며
# 최종 마지막 줄에서의 최대 값을 정답에 넣으면 된다.

def solution(triangle):
    answer = 0
    
    dp = [[0] * (i+1) for i in range(len(triangle))]               # dp 배열 triangle의 크기 만큼 0으로 초기화
    
    dp[0][0] = triangle[0][0]                                      # 첫 초깃값 지정
    
    for i in range(1, len(triangle)):                              # 대각선으로 오른쪽, 왼쪽 값들을 더해가므로
        for j in range(i):                                         # 각 열에서
            dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j])  # 현재 위치와
            dp[i][j+1] = dp[i-1][j] + triangle[i][j+1]             # 바로 옆의 위치의 값들을 각 최대 값으로 최신화 해가며
    
    answer = max(dp[-1])                                           # 최종 마지막 줄에서의 최대 값을 정답에 넣으면 된다.
    
    return answer