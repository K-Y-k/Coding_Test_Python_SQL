operate_timer = [300, 60, 10]        # 타이머 설정된 시간 배열로 선언
count = 0                            # 결과 값 변수 선언

T = int(input())                     # 입력 값 선언

if T % 10 != 0 :                     #  0으로 나누어 떨어지지 않을 경우 -1 출력
    print(-1)

else :                               #  나누어 떨어질 경우
    for i in operate_timer :         # 최소 횟수이므로 큰 원소 값부터 나누어 반복 횟수 출력
        count = T // i               # 각 항마다 나눈 값 결과 변수에 넣고
        T -= count * i               # T는 이미 구한 항의 나눈 값 x T(초)를 뺀 값으로 변경
        print(count, end = ' ')      # 각 항 결과 변수 값 출력