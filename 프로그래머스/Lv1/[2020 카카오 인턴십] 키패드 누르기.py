# 딕셔너리에 각 키패드의 위치를 좌표로 저장한다.
# 각 케이스에 맞게 조건을 잘 설정하면 된다.
# CASE1: 1, 4, 7일 때는 왼손 엄지손가락
# CASE2: 3, 6, 9일 때는 오른손 엄지손가락
# CASE3: 2,5,8,0은 현재 왼손/오른손 엄지손가락의 위치에서 가까운 쪽의 손가락
#       CASE3-1: 현재 왼손/오른손 엄지손가락 두 위치가 동일하면 주어진 주 손잡이의 손가락
 

def solution(numbers, hand):
    answer = ''
    
    position = {                             # 딕셔너리에 각 키패드의 위치를 좌표로 저장
             1:(0,0), 2:(0,1),   3:(0,2),
             4:(1,0), 5:(1,1),   6:(1,2),
             7:(2,0), 8:(2,1),   9:(2,2),
           '*':(3,0), 0:(3,1), '#':(3,2)
        }
    
    position_left = position['*']            # 처음 왼손 엄지손가락 위치는 *에 있다고 했으므로 미리 초기화
    position_right = position['#']           # 처음 오른손 엄지손가락 위치는 #에 있다고 했으므로 미리 초기화
   
    for i in numbers:                        # 주어진 번호 조회
        if i in [1, 4, 7]:                   # 해당 번호가 1,4,7이면 
            position_left = position[i]      # 왼손 엄지손가락을 누르므로 해당 위치로 지정
            answer += 'L'                    # 결과에 추가

        elif i in [3, 6, 9]:                 # 해당 번호가 3,6,9이면 
            position_right = position[i]     # 오른손 엄지손가락을 누르므로 해당 위치로 지정
            answer += 'R'                    # 결과에 추가

        else:                                # 2,5,8,0이면
            # 각 거리를 피타고라스의 정의로 루트(((x1-x2)+(y1-y2))^2) 공식 적용
            left_distance = ((abs(position[i][0] - position_left[0]) + abs(position[i][1] - position_left[1]))**2)**0.5 
            right_distance = ((abs(position[i][0] - position_right[0]) + abs(position[i][1] - position_right[1]))**2)**0.5 
            
            # 좀 더 위보다 간단하게 x좌표끼리의 차이 + y좌표끼리의 차이를 더한 것끼리 비교도 가능
            # left_distance = abs(position[i][0] - position_left[0]) + abs(position[i][1] - position_left[1]) 
            # right_distance = abs(position[i][0] - position_right[0]) + abs(position[i][1] - position_right[1]) 
            

            if left_distance < right_distance:   # 왼쪽 엄지손가락 위치가 더 가까우면 왼쪽 엄지손가락으로 적용
                position_left = position[i]      
                answer += 'L'                   

            elif left_distance > right_distance: # 오른쪽 엄지손가락 위치가 더 가까우면 오른쪽 엄지손가락으로 적용
                position_right = position[i]     
                answer += 'R'                   

            else:                                # 같으면주 주 손잡이의 손가락으로 적용
                if hand == 'left':
                    position_left = position[i]
                    answer += 'L'
                else:
                    position_right = position[i]
                    answer += 'R'

    
    return answer


# 위 피타고라스 정의보다 좀 더 간단하게하기 = x좌표끼리의 차이 + y좌표끼리의 차이를 더한 것끼리 비교도 가능
# left_distance = abs(position[i][0] - position_left[0]) + abs(position[i][1] - position_left[1]) 
# right_distance = abs(position[i][0] - position_right[0]) + abs(position[i][1] - position_right[1]) 
            