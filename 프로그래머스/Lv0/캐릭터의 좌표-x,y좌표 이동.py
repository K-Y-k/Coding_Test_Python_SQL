# 내가 푼 방식
# board 판의 주어진 x,y 좌표에서 나누기 2를 한 몫이 - + 범위의 x,y좌표의 최대 범위이고
# 각 이동 명령어가 올 때 명령을 적용한 연산 값이 최대 범위를 벗어나지 않았으면 적용하였다.


def solution(keyinput, board):
    answer = []
    board_max_X = board[0]//2              # board 판의 주어진 x,y 좌표에서 나누기 2를 한 몫이 - + 범위의 x,y좌표의 최대 범위이고
    board_max_Y = board[1]//2

    a = [0, 0]
    
    for i in keyinput:
        if i == "up":                      # 각 이동 명령어가 올 때 
            if a[1]+1 <= board_max_Y:      # 명령을 적용한 연산 값이 최대 범위를 벗어나지 않았으면 적용하였다.
                a[1] += 1
        elif i == "down":
            if a[1]-1 >= -board_max_Y:
                a[1] -= 1
        elif i == "left":
            if a[0]-1 >= -board_max_X:
                a[0] -= 1
        elif i == "right":
            if a[0]+1 <= board_max_X:
                a[0] += 1
        
            
    answer.append(a[0])
    answer.append(a[1])
    

    return answer