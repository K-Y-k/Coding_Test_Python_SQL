# 집들의 위치들이 원의 형태이므로
# 첫 집을 터는 경우와 마지막 집을 터는 경우 2가지 케이스에 따른 최대 값을 추출해야한다.

def solution(money):
    answer = 0
    
    # 첫 집을 터는 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    
    for i in range(1, len(money)-1): # 첫 집을 털었으므로 마지막 집은 이웃이라 제외해야한다.
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i]) # 현재 집의 옆집을 털어왔을 때의 최대 값과 현재 집 + 옆옆집을 털었을 때의 최대 값중의 최대 값을 넣어준다.
    

    # 마지막 집을 터는 경우
    dp2 = [0] * len(money)
    dp2[0] = 0
    
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    
    answer = max(max(dp1), max(dp2)) # 두 케이스에서의 최대 값들에서의 최대 값을 넣기
    
    return answer