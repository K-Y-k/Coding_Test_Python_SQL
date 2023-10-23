# 문제 조건 잘보자
# 문제 조건에서 시간은 1시~12시간제로 된다고 했으므로 필요한 조건

T = int(input())

for test_case in range(1, T + 1):
    a_hour, a_minute, b_hour, b_minute = map(int, input().split())
    
    total_minute = a_minute + b_minute
    answer_minute = total_minute % 60

    plus_hour = total_minute // 60
    answer_hour = a_hour + b_hour + plus_hour
    

    # 문제 조건에서 시간은 1시~12시간제로 된다고 했으므로 필요한 조건
    if answer_hour > 12:
        answer_hour -= 12
    
    print('#' + str(test_case), answer_hour, answer_minute)