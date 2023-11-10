# 딕셔너리에 미리 각 요일에 따른 일요일까지의 날짜 차이를 저장하고
# 입력된 날짜에 따른 딕셔너리 값을 출력

T = int(input())
        
for test_case in range(1, T + 1):
    dic = {'SUN':7, 'SAT':1, 'FRI':2, 'THU':3, 'WED':4, 'TUE':5, 'MON':6}
    
    week = str(input())
    
    print('#' + str(test_case), dic[week])
