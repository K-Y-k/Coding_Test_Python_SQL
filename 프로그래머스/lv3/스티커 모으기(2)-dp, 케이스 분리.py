# 순열을 이용해서 모든 경우의 수를 가져오고
# 처음 스티커 값부터 넣는 케이스와 두번째 스티커 값부터 넣는 케이스 2가지로 분리하여 dp를 구한다.
# dp 점화식은 이전 위치의 값과 현재 위치-2의 값 + 현재 값을 넣은 값 중 최대 값으로 넣는다.
# 처음 스티커 값부터 넣는 케이스는 점화식을 적용하기 위해 첫번째 값과 두번째 값까지 수동으로 넣어준다.

def solution(sticker):                   
    answer = 0
    
    if len(sticker) == 1:                                      # 스티커가 1개인 경우의 예외처리
        answer = sticker[0]
    else:
        dp_1 = [0] * len(sticker)
        dp_1[0] = sticker[0]
        dp_1[1] = max(sticker[0], sticker[1])                  # 처음 스티커 값부터 넣는 케이스는 점화식을 적용하기 위해 첫번째 값과 두번째 값까지 수동으로 넣어준다.

        dp_2 = [0] * len(sticker)
        dp_2[1] = sticker[1]

        
        for i in range(2, len(sticker)-1):
            dp_1[i] = max(dp_1[i-1], dp_1[i-2] + sticker[i])   # dp 점화식은 이전 위치의 값과 현재 위치-2의 값 + 현재 값을 넣은 값 중 최대 값으로 넣는다.

        for i in range(2, len(sticker)):
            dp_2[i] = max(dp_2[i-1], dp_2[i-2] + sticker[i])

        answer = max(max(dp_1), max(dp_2))
        
    
    return answer