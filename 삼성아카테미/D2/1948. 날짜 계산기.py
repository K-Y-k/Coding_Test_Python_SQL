# 각 월의 날짜를 저장한 딕셔너리를 선언하고
# 문제에서 주어진 시작 월 ~ 끝나는 월을 루프를 돌려 딕셔너리로 저장한 각 월의 최대 일을 더해준다.
# 시작 월일 때는 시작 일을 뺀 값을 더해주고 
# 끝나는 월일 때는 끝나는 일만 더해준다.

T = int(input())

for test_case in range(1, T + 1):
    day_dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    a_month, a_day, b_month, b_day = map(int, input().split())
    answer = 0
    
    for i in range(a_month, b_month+1):
        if i == a_month:
            answer += day_dic[i] - a_day + 1
        elif i == b_month:
            answer += b_day
        else:
            answer += day_dic[i]
   
    print('#' + str(test_case), answer)