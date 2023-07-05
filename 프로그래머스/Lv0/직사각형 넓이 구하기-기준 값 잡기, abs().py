# 내가 푼 방식
# 첫 좌표의 x와 y를 기준 값을 잡고
# 다음 좌표들을 조회하면서 각 좌표의 x,y값이 기준 값의 x,y와 다를경우
# x가 다르면 너비를 구할 수 있게 되고
# y가 다르면 높이를 구할 수 있게 된다.


def solution(dots):
    answer = 0
    
    temp_x = dots[0][0]                    # 첫 좌표의 x와 y를 기준 값을 잡고
    temp_y = dots[0][1]
    
    for i in dots:                         # 다음 좌표들을 조회하면서
        if i[0] != temp_x:                 # x가 다르면 너비를 구할 수 있게 되고
            width = abs(i[0] - temp_x)
        elif i[1] != temp_y:               # y가 다르면 높이를 구할 수 있게 된다.
            height = abs(i[1] - temp_y)

    answer = width * height
    
    
    return answer