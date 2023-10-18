# 파이썬은 switch문이 없기 때문에
# 딕셔너리에 월에 따른 최대 날짜를 담고 
# 받아온 월, 일에 따른 조건 처리를 해준다.


T = int(input())

for test_case in range(1, T + 1):
    a = str(input())
   
    # 딕셔너리에 월에 따른 최대 날짜를 담고 
    day_dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    year = a[0:4]
    month = a[4:6]
    day = a[6:8]
    
    # 받아온 월, 일에 따른 조건 처리를 해준다.
    if  0 < int(month) < 13 and 0 < int(day) < day_dic[int(month)]+1:
        answer = year + '/' + month + '/' + day
    else:
        answer = '-1'
        
    print('#' + str(test_case), answer)