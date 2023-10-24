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